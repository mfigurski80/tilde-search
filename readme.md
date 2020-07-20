# Tilde Search Engine

Search engine for tilde-based websites

## Discovery

Responsible for:

* Discovering + temp storing users
* Discovering + temp storing public websites

## Crawler

Not creepy at all. Responsible for:

* Downloading and creating per-word document-frequency dictionary for tf-idf
* Storing which websites have been tagged with timestamp and hash of content
* Pulling keywords and tagging websites into general tag dictionary

Content explanantion

* `tokenize_corpus` and `Porter` files - are responsible for cleaning corpus data
into stemmed tokens. Needs `stopwords.txt` file in same dir
* `data` file - interfaces with numerous text and json files for easy data
management
* `parse_url` file - handles html, including requests and parsing text and
metadata
* `init_freq_dir` file - creates and/or updates document frequency dictionary
* `crawl` file - goes thru urls and gathers tags + metadata for dictionaries


This document last updated: Jul 18 2020
