# hafez-poem-generation-wrapper
This repository is a wrapper for calling the API provided by this repository to generate poetry using Hafez: https://github.com/shixing/poem

# Setup
Follow the instructions in the above stated repo and make sure the API server is listening on *0.0.0.0:8080* <br>
Setup a word list with topics by creating a new file containing one topic in each line and save it as *word_list.txt*
After that you can run the following command to generate 1000 poems which are saved in *hafez_poems.txt*:
```shell
python generate.py
```
