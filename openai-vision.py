from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    # "text": "Can you extract the information presented inside this image? Return only the results in JSON format. Do not wrap in markdown.",
                    # "text": "Can you extract the information presented inside this image? Return a summary containing the important details. Present it in a way that is helpful for people with visual problems.",
                    "text": "Can you extract the information presented inside this image? Return a summary containing the important details. Present it in a way that is to be delivered in speech for people with visual problems.",
                },
                {
                    "type": "image_url",
                    # REACTJS DEVELOPER
                    "image_url": {
                        "url": "https://scontent-mnl1-2.xx.fbcdn.net/v/t39.30808-6/414706390_2531934306984189_906437400580990266_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=c42490&_nc_eui2=AeHGLSsaELL674sllq77SkcrG2nf6lXjqlAbad_qVeOqUM2coN04g8ntRJjc5krDGegTuWCtYJY7lpilFjxegO6z&_nc_ohc=sOdDRJsdOUAAX93_cQ3&_nc_ht=scontent-mnl1-2.xx&oh=00_AfDottxFfyTdzEjrUCL_3gm0P4xYBnHiN1pxrFZqLHJZTA&oe=6592744C",
                    },
                    # ABS-CBN Boxing
                    # "image_url": {
                    #     "url": "https://scontent-mnl1-2.xx.fbcdn.net/v/t39.30808-6/399514156_762560982585827_5900333409444941554_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeFkUjkKzg4qEa7Th8PUurbFAdFqN741SHIB0Wo3vjVIch8OcVyOhR0gnCJUCFy-zZ70cOvL7ZuoxfVxNK0A37da&_nc_ohc=jkNg9w6f_14AX8zEqXP&_nc_ht=scontent-mnl1-2.xx&oh=00_AfClFk5OtCxwEBu9niwU2ByQET5WQzvBxvn9b0u0l55z3w&oe=6592CB14",
                    # },
                    # WORDS OF ADVICE
                    # "image_url": {
                    #     "url": "https://scontent-mnl1-2.xx.fbcdn.net/v/t39.30808-6/406811502_122152592888010180_415095826402084819_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeEAbDfajuu1Iy_5rQDIFHYJee0VXrVFf5Z57RVetUV_lluKn-AlVg7SzXKViPFmepUx3EzDyo91hH1ea_0DkYV_&_nc_ohc=TFZEjz38N4oAX80n_Ld&_nc_ht=scontent-mnl1-2.xx&oh=00_AfDGYd5jdAaxnlfThj_NRfpkP_hVjdibI1cGy7RTRCoBRA&oe=6592E85B",
                    # },
                    # HERD IMMUNITY
                    "image_url": {
                        "url": "https://scontent-mnl1-2.xx.fbcdn.net/v/t1.6435-9/192790903_206580917976783_7000397841369726407_n.png?_nc_cat=100&ccb=1-7&_nc_sid=0bb214&_nc_eui2=AeE-0ttR0KnifQK5JAYCabFHIlfKcthH-k4iV8py2Ef6TlUqjzFQ-8Ov576QXceHMsvJazS6pFFTFaCFjwrqbIbY&_nc_ohc=NKFQjp3hdgUAX8xHFKK&_nc_ht=scontent-mnl1-2.xx&oh=00_AfBcx8OekvZOHUUESSVo6ZrO7J0wrohCw0dwqmj7Dlk97w&oe=65B4E0F1",
                    },
                },
            ],
        }
    ],
    # max_tokens=300,
)

print(response.choices[0].message.content)
