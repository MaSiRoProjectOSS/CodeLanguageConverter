# Automatic code conversion using generative AI

[English](./README_en.md)

In this repository, we've created a feature that uses generative AI to automatically translate the language of your code.

#### What you can do

- Convert from Python to C++

## Required Libraries

- Python
  - Tested with version 3.11.3
  - OpenAI or Anthropic or Ollama
  - Jupyter Notebook
  - networkx

### How to install the library

In the Python environment, execute the following.

```
pip install notebook
pip install openai
pip install anthropic
pip install ollama
pip install networkx
```

### About GNU G++

To check the generated C++ code, we use GNU G++, which can be used by installing MinGW on Windows.
Make sure that "g++" is available in the terminal beforehand.

## About the use of Generative AI

This repository uses the Open AI, Anthropic, and Ollama. For information on how to use them and activate your API key, please refer to the documentation.

## How to use

Open "convert_code_language.ipynb", edit it as needed, and run it.

### Conditions for Python code files to be converted

- The file must contain the definition of the class.
- There must be only one class in a file.
- Do not using an external library (extension module).
- Specify the Python code folder to be converted into an argument of PythonDependencyAnalyzer
- You must have Python code in that folder.

## Support

Please create a new issue and let us know the details.

## Contribution

We welcome pull requests from the community. If you're thinking about making a significant change, start by opening an issue to start a discussion about the proposed fix.

Also, when you submit a pull request, make sure that the relevant tests are updated or added as needed.

## License

[MIT License](./LICENSE.txt)

