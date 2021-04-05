#!/usr/local/bin/guile -s
!#
(newline)
(define lis (command-line))
(define arg1 (list-ref lis 1))
(define arg2 (list-ref lis 2))
(display arg1)(newline)
(display arg2)(newline)
(use-modules (ice-9 regex))
(define file (open-input-file arg1))
(use-modules (ice-9 textual-ports))
(define text (get-string-all file))
(define pattern "module[[:space:]]fa((.|\n)*)?endmodule")
(define nom (map match:substring (list-matches pattern text)))
(define first (list-ref nom 0))
(display  first)
(newline)
;((?!endmodule).)*
