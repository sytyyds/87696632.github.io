import openai
   openai.api_key = "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"

   def generate_post():
       response = openai.ChatCompletion.create(
         model="gpt-4",
         messages=[{
           "role": "user", 
           "content": "用天蝎座擅长的深度分析方式讲解Python装饰器"
         }]
       )
       return response.choices[0].message.content

   if __name__ == "__main__":
       post = generate_post()
       with open(f"_posts/{datetime.date.today()}-decorator.md", "w") as f:
           f.write(post)
