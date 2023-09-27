TIL Example Post 3

---

In my second week of exploration with Open Source, I was asked to write a command-line program which converts .txt files to .html. When I completed my working prototype of the app, I found **Yumei** in the Slack open source group channel and we agreed to test each others' code.

This is my first time raising issues in another person's project and also my first time fixing the closing the issues she raised in my project. Although the programs we each wrote are short and simple, this really got me more comfortable with collaborating with others on GitHub. Also, it was fun to see how we both created a similar running program; however the code is completely different.

I chose to write my program in *Python* while she used *Java*. Aside from syntax differences, she has much more exception handling in her code compared to mine. It made me think that I should add more exception handling to my own code. Having another person test my code definitely helps to find more issues! She discovered that I missed implementing the spec for deleting the default output folder at the start of the run. Also, she uses a VS Code extension called Pylint which helped to find many problems with my code. Pylint found many issues with my code which were not best practice, such as not specifying an encoding when reading from a file, or using an f-string that does not have any interpolated variables.

When I tested **Yumei**'s program, I was able to find some bugs that she could not find herself. For example, I am a Windows user and she is a Mac user. There is an installation step that is not applicable to Windows users. I also found a runtime error that occurred when I specified the output flag but gave no output directory.

We were able to close all our issues after our successful collaboration! I learned from looking at her code more ways to handle exceptions and more ways to find bugs (using the Pylint extension). I also got some insight on how the logic I wrote in Python can be done in Java. Finally, this collaboration not only helped our programming skills but also our testing, documentation, and communication skills as we worked together to identify and fix issues.