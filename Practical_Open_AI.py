from openai import OpenAI #imported OpenAI


### Zero-shot prompting ###
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Here i have Defined a multi-line prompt to classify sentiment
prompt = """sentiment classification using reviews from an online shoe store called Toe-Tally Comfortable.:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

### OUTPUT ###
# Here's a sentiment classification for each of the reviews provided:

# 1. **Unbelievably good!** - **Positive**
# 2. **Shoes fell apart on the second use.** - **Negative**
# 3. **The shoes look nice, but they aren't very comfortable.** - **Neutral/Negative** (mixed sentiment, but leans negative due to comfort issue)
# 4. **Can't wait to show them off!** - **Positive**

#If you have more reviews or need further analysis.


# Created a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model = "gpt-4o-mini",
  messages = [{"role": "user", "content": prompt}],
  max_completion_tokens = 100
)

print(response.choices[0].message.content)


### One-shot prompting ###
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# I have Added the example to the prompt
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! = 5
3. Shoes fell apart on the second use. = 1
4. The shoes look nice, but they aren't very comfortable. = 2
5. Can't wait to show them off! = 5"""

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)


### Few-shot prompting ###
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Here i have Added the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 5
4. Shoes fell apart on the second use. = 2
5. The shoes look nice, but they aren't very comfortable. = 1
6. Can't wait to show them off! = 5"""

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)


### creatd my very own AI-powered chatbot ###

client = OpenAI(api_key="<OPENAI_API_TOKEN>") #here i taken my api connection
#here i added 2 variable in in list dict and list.
messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}] #assigning the ai model
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."] #making the req to the user.

# Loop over the user questions
for q in user_msgs: #user_msgs
    print("User: ", q)
    
    # Created a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Created the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")
#  User:  Explain what pi is.
# Assistant:  Pi (π) is a mathematical constant representing the ratio of a circle's circumference to its diameter. It's approximately equal to 3.14159 and is an irrational number, meaning it has an infinite, non-repeating decimal expansion. Pi is used in various mathematical calculations involving circles, such as determining the area (A = πr²) and the circumference (C = 2πr), where r is the radius. 

# User:  Summarize this in two bullet points.
# Assistant:  - Pi (π) is the ratio of a circle's circumference to its diameter, approximately equal to 3.14159, and is an irrational number.
# - It is used in calculations involving circles, such as area (A = πr²) and circumference (C = 2πr). 