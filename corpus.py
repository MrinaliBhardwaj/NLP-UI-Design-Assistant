import json
from preprocess import clean_text

wiki = clean_text("""User experience (UX) is how a user interacts with and experiences a product, system, or service. It includes a person's perceptions of utility, ease of use, and efficiency. Improving user experience is important to most companies, designers, and creators when creating and refining products because negative user experience can diminish the use of the product.

According to Nielsen Norman Group, 'user experience' includes all the aspects of the interaction between the end-user with the company, its services, and its products.

The international standard ISO 9241 defines user experience as a user's perceptions and responses resulting from use.""")

blog = clean_text("""The first requirement for an exemplary user experience is to meet the exact needs of the customer, without fuss or bother. Next comes simplicity and elegance that produce products that are a joy to use. True user experience goes beyond giving users what they say they want and focuses on meaningful interaction and usability.""") 

pdf1 = clean_text("""UX design principles include usability goals, Norman’s interaction model, and execution-evaluation cycles. These frameworks help structure UX design by guiding how users perform actions and evaluate system responses. Planning and matching user mental models are essential in UX design.""") 

pdf2 = clean_text("""User experience (UX) and user interface (UI) are critical aspects of system design. UX focuses on usability, accessibility, and user satisfaction, while UI focuses on visual and interactive elements. Understanding both helps create better digital products and improve user interaction.""") 

corpus = [
    {
        "source": "Wikipedia",
        "topic": "UX Design",
        "content": wiki[:2000]
    },
    {
        "source": "Blog",
        "topic": "UX Design",
        "content": blog[:2000]
    },
    {
        "source": "PDF 1",
        "topic": "UX Design",
        "content": pdf1[:2000]
    },
    {
        "source": "PDF 2",
        "topic": "UX Design",
        "content": pdf2[:2000]
    }
]

with open("corpus.json", "w") as f:
    json.dump(corpus, f, indent=4)

print("Corpus created successfully!")