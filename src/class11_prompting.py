from transformers import pipeline, set_seed
set_seed(42)

from transformers import AutoTokenizer, AutoModelWithLMHead
  
#tokenizer = AutoTokenizer.from_pretrained("flax-community/dansk-gpt-wiki")

#model_da = AutoModelWithLMHead.from_pretrained("flax-community/dansk-gpt-wiki")

generator = pipeline('text-generation', model="gpt2") #, tokenizer=tokenizer)  # Note that a larger model is likely to produce a better result.

# new york times article
TEXT = """According to a number of blue parties and Frie Grønne, the Detention Service's Intelligence Service will try to recreate the text messages that Mette Frederiksen and three officials at the top of the Prime Minister's Office have deleted.

At a meeting on Friday at 9.30 the proposal must be discussed.

Specifically, they want the intelligence service's Center for Cyber ​​Security to recover the messages from the mink case in the period September-December 2020, after the police IT technicians failed.

"In addition, we also think it is a good idea to get assistance and help from private IT experts," says the Liberal Party's political spokesperson Sophie Løhde.

On Wednesday, Minister of Justice Nick Hækkerup repeatedly refused in the Folketing Hall to answer questions about how the police had tried to recover the messages, as well as which department in the police had made the attempt.

"We do not know what order the police have been given. We do not know if only programs or what is called manual extraction have been tried, "says the Conservatives' Mai Mercado.

On the left, Frie Grønne supports the proposal to let the Defense Intelligence Service and possibly private companies try.

“We support because we want openness and transparency. It serves democracy, and it serves the left to have the same standard as if it were a bourgeois prime minister, which we were examining, "says party leader Sikandar Siddique and elaborates:

"It had been a process in which the Prime Minister has been headstrong and had an enormous amount of power, therefore it is completely legitimate to investigate what has happened."

If a majority can be formed at the meeting of the Committee of Inquiry on Friday, according to Mai Mercado, there are different approaches.

The parties behind the majority can send a letter to the prime minister calling for the Center for Cyber ​​Security and private companies to get the try.

Otherwise, the majority can make a proposal about it, and in the end you can choose to open the Mink Commission's terms of reference and let it be included, Mai Mercado explains.

Jacob Kaarsbo is former head of analysis at the Defense Intelligence Service. He estimates that the service has the potential to recreate the text messages.

"In the Defense Intelligence Service, we were always told that all these text messages and data from mobiles could be recovered. So I think it sounds weird when the police have not been able to recover the text messages. It seems that they have not made a particularly careful attempt, "says Jacob Kaarsbo, expert in communication security.

New Civic and Liberal Alliance also backs the proposal.

SF will only back up if it is a wish from the Mink Commission, says Karina Lorentzen.

B.T. trying to get a comment from the Social Democrats, the Unity List and the Radical Left.
"""

prompt = "tl;dr"

output = generator(TEXT + prompt, 
                   max_length=630,  # max_length should be adaptable to model input size
                   num_return_sequences=1
                   )

