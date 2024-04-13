# MEMORIZE: Local Language Model Assisted Word Memorization

![Screenshot 2024-04-13 at 13.20.09](https://cdn.jsdelivr.net/gh/TANG617/images@master/20240413132042lQsJPuScreenshot%202024-04-13%20at%2013.20.09.png)



- Optimize the workflow personally, display any information you need
- Deploy locally without requirements of any API
- Choose from a variety of LLMs, including LLAMA2, Phi, etc
- Adapt for multi-language including but not limited to English or Chinese

## Project Struct

- `source`: Source `json`file of vocabulary
- `tex`: Generated tex file
- `pdf`: Generated pdf file
  - `noline`: No dividing line between 2 words
  - `nochinese`: No Chinese meaning of the word itself

## PipeLine

![image-20240413134452977](https://cdn.jsdelivr.net/gh/TANG617/images@master/20240413134453pnquDSimage-20240413134452977.png)

- Use Ollama(https://ollama.com) as the backend of LLM, which is capable of multiple LLM and hardware acceleration (like CUDA). Also, it's able to deploy LLM remotely and use REST API to access.
  - As for me, I choose to deploy Llama-2-7b with RTX3080 CUDA. The performance is satisfied, each phase or sentence takes 3-5 seconds.
- Source of the IELTS/GRE vocabulary comes from the Internet.

### Example

| <img src="https://cdn.jsdelivr.net/gh/TANG617/images@master/20240413135605rffN35image-20240413135605874.png" alt="image-20240413135605874" style="zoom:50%;" /> | Word itself <br />Upper number indicates the level of difficulty<br />Sentences corresponding to its difficulty <br />Phases corresponding to its difficulty |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

#### Recommandation

- Use English description rather than Chinese translation
- Guess the accurate meaning by sentences and phases
- Validate the guessing meaning by taking more sentences and phases into account

## TODO

- More features
  -  mark the level of memorization 
  - real-time optimization
- Convert each option to paramter without modifying the code
- Better prompts for LLM
- Store generated text to database rather than stream into `.tex` file ( reduce failure)
- Convert to Anki format