-module(hello).        % 模块名要和文件名一致
-export([say/0]).      % 导出 say 函数

say() ->
    io:format("Hello, Erlang!~n").

