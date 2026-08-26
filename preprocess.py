import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def clean_text(text):
    """Remove invalid Unicode surrogates (broken emojis)."""
    return text.encode("utf-16","surrogatepass").decode("utf-16","ignore")

def process_posts(raw_file_path,processed_file_path="Data/processed_posts.json"):
    enriched_posts=[]
# open raw file
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)     #load file

    # extract some extra info
        for post in posts:
            post["text"] = clean_text(post["text"])
            metadata= extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

            # Save processed file
        with open(processed_file_path, "w", encoding="utf-8") as file:
            json.dump(enriched_posts, file, ensure_ascii=False, indent=4)

        print(f"Processed {len(enriched_posts)} posts.")
        return enriched_posts

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag]    for tag in current_tags}  # set comprehension
        post['tags']=list(new_tags)

def get_unified_tags(posts_with_metadata):
    unique_tags = set()   # remove duplicate data
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
    unique_tags_list = ','.join(unique_tags)
    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
        1. Tags are unified and merged to create a shorter list. 
           Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
           Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
           Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
           Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
        2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
        3. Output should be a JSON object, No preamble
        3. Output should have mapping of original tag and the unified tag. 
           For example: {{"Jobseekers": "Job Search",  "Job Hunting": "Job Search", "Motivation": "Motivation}}

        Here is the list of tags: 
        {tags}
        '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res






def extract_metadata(post):
    # prompt creation
    template = '''
       You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
       1. Return a valid JSON. No preamble. 
       2. JSON object should have exactly three keys: line_count, language and tags. 
       3. tags is an array of text tags. Extract maximum two tags.
       4. Language should be English or Hinglish (Hinglish means hindi + english)

       Here is the actual post on which you need to perform this task:  
       {post}
       '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
# pipe op (|) - create a chain means supplying prompt to the llm

    response = chain.invoke(input={'post':post})
    try:
        json_parser = JsonOutputParser()
        res= json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context is too big.Unable to parse jobs.")
    return res


    return {
        'line_count':10,
        'language':'English',
        'tags':['Mental Health','Motivation']
    }


if __name__=="__main__":
    process_posts("Data/raw_posts.json","Data/processed_posts.json")
