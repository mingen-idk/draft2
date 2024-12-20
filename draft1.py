import pandas as pd

df_CCA = pd.read_csv ('/home/mingen/Downloads/data/CocurricularactivitiesCCAs.csv')

df_CCA2 = pd.read_csv ('/home/mingen/Downloads/data/CocurricularactivitiesCCAs(1).csv')

general_info = pd.read_csv ('/home/mingen/Downloads/data/Generalinformationofschools(1).csv')

general_info2 = pd.read_csv ('/home/mingen/Downloads/data/Generalinformationofschools(2).csv')

subjects_offered = pd.read_csv ('/home/mingen/Downloads/data/SubjectsOffered.csv')


def main():
    cca = input("Enter your current CCA: ")
    interests = input("What are your interests? / What do you want to do in future? : ")
    skills = input("What are your skills or strengths? : ")
    scores = input("What is your current L1 R5 score? : ")
    live = input("Which town do you in? : ")
    preference = input("Do you prefer a theory-focused type of study or learning more practical skills? : ")


    # Split the interests by comma and strip whitespace
    interests_list = [i.strip() for i in interests.split(',')]

    # Print to confirm what was gathered 
    print("You entered:")
    print(f"CCA: {cca}")
    print(f"Preference: {preference}")
    print(f"Interests: {interests}")
    print(f"Skills: {skills}")
    print(f"Scores: {scores}")
    print(f"Location: {live}")

        
    import openai

    # Replace 'your-api-key' with your actual OpenAI API key
    openai.api_key = ""

    prompt_test = f"""I am from Chung Cheng High School. My CCA is {cca}. My interest are {interests}. \
    My skills are {skills}. My L1R5 is {scores}. I live in {live}. I prefer learning {preference}. \
    Can you provide a school (JC/Poly) that is near me and recommended for me? and courses provided by the school?"""
    print(prompt_test)

    response = openai.ChatCompletion.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_test}
                ],
            max_tokens=500
        )
        
    print
    # Print the assistant's reply
    print(response.choices[0].message['content'].strip())





if __name__ == "__main__":
        main()
