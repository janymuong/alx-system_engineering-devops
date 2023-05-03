# regex
> `Regular expressions` consist of a pattern of *character sequence* that can be used to match and manipulate text - a specific sequence of characters string. 

This is a directory on ***regex***; with scripts written in `Ruby`, and the default `Oniguruma` library which provides a rich set of features and syntax for working with `regex patterns`.

| Regex Pattern | Description |
|--------------|-------------|
| `/hello/` | regex pattern matches the string "hello" in the text. |
| `/[aeiou]/` | matches any vowel character in the text. |
| `/[0-9]+/` | matches one or more digit characters in the text. |

> these patterns can be used with methods like `scan` or `match` to find and manipulate text in Ruby.



## Basic Regex Syntax in Ruby

`usage in a script`: 
```bash
$ cat script.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
$
```


## `appendix: general Ruby code syntax`
- `puts` - this is a Ruby method used to output a string to the console.
- `ARGV[0]` - accesses the first element of the `ARGV` array, which is an array of command-line arguments passed to the script.
- `.scan(/regex-pattern/)` - this searches for any occurrence of the "regex-pattern" in the argument provided to the script. the `scan` method returns an array of all matches found.
- `.join` - a method that joins the elements of an array into a single string.
