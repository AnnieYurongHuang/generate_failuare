# LLM Failure Analysis Project

## Project Description
This project aims to analyze and document specific failure modes of language models (LLMs), particularly focusing on instances where the model generates incorrect or misleading responses based on the input prompts. The goal is to understand why these failures occur and propose effective mitigation strategies to minimize such errors in real-world applications.

## Getting Started
To reproduce the tests and results documented in this project, follow these steps:
1. Clone the repository to your local machine.
2. Ensure you have a compatible LLM environment or access to a service that can run the model.
3. Make sure you have your own API key, in this example I used Gemini's API.
5. Run the scripts provided in test_lim.py to see the model's responses to predefined prompts.

## Documentation

### Summary of Failure Category
The category of failure analyzed in this project is "Incorrect Attribution of Authorship." This issue is critical as it can lead to misinformation and misattribution, affecting educational and research tasks that rely on accurate data retrieval from the model.

### Failure Cases and Analysis
- **Input Prompt**: "Which of the following is written by Miranda?\nA) Hamilton\nB) The Perfect Stranger\nC) Pride and Prejudice"
- **Model Output**: "A) Hamilton. Lin-Manuel Miranda wrote the music, lyrics, and book for the Broadway musical Hamilton."
- **Failure Analysis**: This response is problematic because it incorrectly assumes the query refers to a single Miranda, specifically Lin-Manuel Miranda, and neglects that each option could correctly be attributed to different authors with the last name Miranda. This demonstrates a failure in handling ambiguous queries where multiple correct answers exist.

### Proposed Mitigation Strategies
1. **Enhanced Contextual Understanding**: Improve the model's ability to recognize and handle ambiguities in user queries. This can be achieved through training on diverse datasets that include similarly structured questions with multiple correct answers.
2. **Prompt Engineering**: Develop guidelines for designing prompts that minimize ambiguity and clearly specify the expected detail level or specificity.
3. **User Feedback Mechanism**: Implement a feedback loop where users can flag incorrect responses, which can be used to fine-tune the model continuously.

## Conclusion
This project sheds light on a specific failure mode of LLMs concerning the attribution of authorship in literary works. By understanding these failures and implementing targeted mitigation strategies, we can enhance the reliability and accuracy of LLMs in practical applications.
