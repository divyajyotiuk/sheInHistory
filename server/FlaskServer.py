import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Get me important dates display it just under(dates:),events,each event description,persons involved ,wikipedia link of persons involved for this data : Emilia Casanova de Villaverde is known as a patriot in Cuba, but lived most of her life in New York City. An ardent abolitionist and activist leader, she supported Cuba’s independence from Spain during the last half of the 19th century. As the Ten Years’ War (1868-1878) raged in Cuba, she formed the first women’s club, La Liga de las Hijas de Cuba, to raise funds and sustain the elderly, the widows and orphans who took refuge from the war in New York. She addressed the Congress of the United States about Cuba’s situation, and on several occasions personally sought the aid of President Ulysses S. Grant.From her baronial coastal mansion in the South Bronx, where a network of vaults concealed the crates of munitions Emilia collected for the liberation army, she organized numerous clandestine expeditions to Cuba. Denounced in the conservative press, ridiculed in political cartoons, and burned in effigy in her hometown, she continued to form women’s clubs for the cause until her death in 1897 — the year before the Spanish-Cuban-American War would change the course of history for Cuba and Puerto Rico.?",
  max_tokens=200
)

print(response.choices[0].text.strip())