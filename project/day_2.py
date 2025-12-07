"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap
name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
Passion = input("Enter your one-liner passion or goal? ").strip()
fav_emoji= input("Enter your favourite emoji? ").strip()
website= input("Enter your website: ")


print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")


style = input("Enter 1, 2 or 3 which you want: ")


def generate_bio(style):
    if style == "1":
        return f"{fav_emoji} {name} | {profession} \n 💓 {Passion} \n {website}"
    elif style == "2":
        return f"{fav_emoji} {name}\n {profession}👩‍💻\n{Passion} \n🔗{website} "
    elif style == "3":
        return f"{fav_emoji*3}\n{name}✅ _- 👩‍💻{profession}📈 \n👉{Passion} \n🕸️{website} \n{fav_emoji*3}"
    
bio = generate_bio(style)

print("\nYour sylish Bio:\n")
print("#" * 50)
print(textwrap.dedent(bio))
print("#" * 50)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()
if save == 'y':
    filename = f"{name.lower().replace(' ', ' _')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
        print("file saved")
elif save =='n':
    print("file not saved")