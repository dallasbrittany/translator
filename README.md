# translator

Trying out SeamlessM4T, which is good for language translation (both text and audio).

## Install and Setup Details (Mac)

### pyenv

If you choose to use `pyenv` to manage your Python versions and don't have everything set up yet:

```
brew update
brew install pyenv
brew install pyenv-virtualenv
```

You may also want to add this to your ~/.zshrc:

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PIPENV_PYTHON="$PYENV_ROOT/shims/python"

plugin=(
  pyenv
)

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Install Python using `pyenv` and (optionally) set it as the global version:

```
pyenv install 3.11.10
pyenv global 3.11.10
```

NOTE: 3.11 is used because 3.12 had compatibility problems with Seamless Communication as of Sept 2024.

### pipenv

Install `pipenv` if you haven't already for the version of Python being used for this project:
```
pip3 install pipenv
```

Set up `Pipfile` using `pipenv` if it's not already set up:
```
pipenv --python 3.11.10
```

To start `pipenv` virtual environment:
```
pipenv shell
```

Install dependencies:

```
pipenv install
```

Exit:

```
exit
```

### Other

You probably also need this:

```
brew install libsndfile
```

You may or may not need this:

```
brew install readline xz
```

## Resources
- [SeamlessM4T](https://ai.meta.com/blog/seamless-m4t/)
- [Seamless Communication Repo](https://github.com/facebookresearch/seamless_communication)
- [Seamless Tutorial](https://github.com/facebookresearch/seamless_communication/blob/main/Seamless_Tutorial.ipynb)
    - Needs some modifications to run on a MacBook.
- [How to Run on MacOS](https://betterprogramming.pub/how-to-run-metas-new-model-seamlessm4t-on-macos-172b84b285e3)
    - Don't follow everything in this. It's out of date.
- [Deployment](https://community.sap.com/t5/technology-blogs-by-sap/deployment-of-seamless-m4t-v2-models-on-sap-ai-core/ba-p/13680013)

## Examples

### T2TT

#### Accents

It does appear to take punctuation into account, and it can infer accents if it has enough information from the punctuation.

```
python t2tt.py spa eng "si yo quiero"
Translated text:
If I want to

python t2tt.py spa eng "si, yo quiero"
Translated text:
Yes, I want to.
```

#### Bias

There's definitely some bias that's obvious in the ENG->SPA translations. It defaults to male for computer programmer and software engineer but defaults to female for teachers. If you tell it you're a man or a woman, it fixes it.

```
python t2tt.py eng spa "I'm a software engineer."
Translated text:
Soy ingeniero de software.

python t2tt.py eng spa "I'm a woman who is a software engineer."
Translated text:
Soy una mujer que es ingeniera de software.

python t2tt.py eng spa "I'm a teacher."
Translated text:
Yo soy maestra.

python t2tt.py eng spa "I'm a man who is a teacher."
Translated text:
Soy un hombre que es un maestro
```