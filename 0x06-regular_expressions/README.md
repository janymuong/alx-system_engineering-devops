# regex
> regular expressions - wildcards on steroids :)

`Regular expressions` consist of a pattern of *character sequence* that can be used to match and manipulate text - a specific sequence of characters string. 

This is a directory on ***regex*** that is rather glib;    
Scripts are written in `Ruby`, and the default `Oniguruma` library which provides a rich set of features and syntax for working with regex patterns.

## Basic Regex Syntax in Ruby

- `/hello/` - matches the string "hello" in the text
- `/[aeiou]/` - matches any vowel character in the text
- `/[0-9]+/` - matches one or more digit characters in the text
> these patterns can be used with methods like `scan` or `match` to find and manipulate text in Ruby.

`usage in a script`: 
```bash
$ cat script.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
$
```

| Command/Code | Description |
|--------------|-------------|
| `#!/usr/bin/env ruby` | `shebang` line tells the system which interpreter to use to execute the script. |
| `puts` | this is a Ruby method used to output a string to the console. |
| `ARGV[0]` | accesses the first element of the `ARGV` array, which is an array of command-line arguments passed to the script. |
| `.scan(/127.0.0.[0-9]/)` | this searches for any occurrence of the IP address "127.0.0." followed by a single digit (0-9) in the argument provided to the script. the `scan` method returns an array of all matches found. |
| `.join` | a method that joins the elements of an array into a single string. |
