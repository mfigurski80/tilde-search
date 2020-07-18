# Tilde Search Engine

Search engine for tilde-based websites

## Database / Data_Queue

Can be found in current `data` folder. The Data_Queue object is a repository for
data about the existence of discovered sites, existence of tagged sites, and
tags generated for each site.

Queries possible from the exported object:

* pop_discovered
* push_discovered
* peek_tagged
* push_tagged
* peek_tag
* push_tag

Note that you can only pop discovered sites, as the list of tagged sites and
tags themselves should never be edited after their creation

This document last changed: Jul 17
