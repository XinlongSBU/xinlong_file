#ifndef __dbg_h__
#define __dbg_h__

#include <stdio.h>
#include <errno.h>
#include <string.h>

#ifdef NDEBUG
#define debug(M, ...)
#else
#define debug(M, ...) fprintf(stderr, "DEBUG %s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#endif

#define clean_errno() (errno == 0 ? "None" : strerror(errno))

#define log_err(M, ...) fprintf(stderr, "[ERROR] (%s:%d: errno: %s) " M "\n", __FILE__, __LINE__, clean_errno(), ##__VA_ARGS__)

#define log_warn(M, ...) fprintf(stderr, "[WARN] (%s:%d: errno: %s) " M "\n", __FILE__, __LINE__, clean_errno(), ##__VA_ARGS__)

#define log_info(M, ...) fprintf(stderr, "[INFO] (%s:%d) " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)

#define check(A, M, ...) if(!(A)) { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

#define sentinel(M, ...)  { log_err(M, ##__VA_ARGS__); errno=0; goto error; }

#define check_mem(A) check((A), "Out of memory.")

#define check_debug(A, M, ...) if(!(A)) { debug(M, ##__VA_ARGS__); errno=0; goto error; }

#endif

/*
是的，这就是全部代码了，下面是它每一行所做的事情。
dbg.h:1-2
防止意外包含多次的保护措施，你已经在上一个练习中见过了。
dbg.h:4-6
包含这些宏所需的函数。
dbg.h:8
#ifdef的起始，它可以让你重新编译程序来移除所有调试日志信息。
dbg.h:9
如果你定义了NDEBUG之后编译，没有任何调试信息会输出。你可以看到#define debug()被替换为空（右边没有任何东西）。
dbg.h:10
上面的#ifdef所匹配的#else。
dbg.h:11
用于替代的#define debug，它将任何使用debug("format", arg1, arg2)的地方替换成fprintf对stderr的调用。许多程序员并不知道，但是你的确可以创建与printf类似的可变参数宏。许多C编译器（实际上是C预处理器）并不支持它，但是gcc可以做到。这里的魔法是使用##__VA_ARGS__，意思是将剩余的所有额外参数放到这里。同时也要注意，使用了__FILE__和__LINE__来获取当前fine:line用于调试信息。这会非常有帮助。
dbg.h:12
#ifdef的结尾。
dbg.h:14
clean_errno宏用于获取errno的安全可读的版本。中间奇怪的语法是“三元运算符”，你会在后面学到它。
dbg.h:16-20
log_err，log_warn和log_info宏用于为最终用户记录信息。它们类似于debug但不能被编译。
dbg.h:22
到目前为止最棒的宏。check会保证条件A为真，否则会记录错误M（带着log_err的可变参数），之后跳到函数的error:区域来执行清理。
dbg.h:24
第二个最棒的宏，sentinel可以放在函数的任何不应该执行的地方，它会打印错误信息并且跳到error:标签。你可以将它放到if-statements或者switch-statements的不该被执行的分支中，比如default。
dbg.h:26
简写的check_mem宏，用于确保指针有效，否则会报告“内存耗尽”的错误。
dbg.h:28
用于替代的check_debug宏，它仍然会检查并处理错误，尤其是你并不想报告的普遍错误。它里面使用了debug代替log_err来报告错误，所以当你定义了NDEBUG，它仍然会检查并且发生错误时跳出，但是不会打印消息了。
*/
