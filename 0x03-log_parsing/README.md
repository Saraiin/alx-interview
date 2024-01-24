<h1>0x03-log_parsing</h1>
<h2> Task :memo::</h2>
Write a script that reads stdin line by line and computes metrics:

1. Input format: (IP Address) - [<date>] "GET /projects/260 HTTP/1.1" (status code> (file size) (if the format is not this one, the line must be skipped)
2. After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- Total file size: File size: (total size)
-  where (total size)> is the sum of all previous (file size) (see input format above)
- Number of lines by status code:
-- possible status code: 200, 301, 400, 401, 403, 404, 405 and 500<br>
-- if a status code doesn’t appear or is not an integer, don’t print anything for this status code<br>
-- format: (status code): (number)<br>
-- status codes should be printed in ascending order<br>
