#!/usr/local/bin/guile -s
!#

(use-modules (ice-9 textual-ports))
(use-modules (ice-9 regex))
;;(use-modules (comment-reducer))

(define (file-read)
  (let ( (verilog-file (list-ref (command-line) 1)) ) ; read verilog filename from command line arg
    (
     let ( (file (open-input-file verilog-file)) ) ; open file-handler
      (get-string-all file) ; read file
      )
    )
  )

(define (regex-pattern-maker)
  ;; syntax of module definition
    (let ((module-start "module[[:space:]]") 
	  (verilog-module (list-ref (command-line) 2))
	  (body "((.|\n)*)?")
	  (endmodule "endmodule"))
		  
      (string-append module-start verilog-module body endmodule)) ; create complete regex
    )
 
;;; implementation of lazy evaluation for regex matching
(define (regex-lazy-eval pattern source-text)
  
  ;;PROCEDURE
  (let ( (temp-string (match-regex pattern source-text)))
    (if (string= "" temp-string)
	"" ; if module does not exist, return empty string
	(let* ( (intermediate-output (string-match "endmodule" temp-string))
		(last-index (match:end intermediate-output))
		)
	  (substring temp-string 0 last-index))
	))
  )

;; proceedure to match regex with text
(define (match-regex pattern t-string)
  (define match-list (map match:substring (list-matches pattern t-string)))
  (if (= (length match-list) 0) "" (list-ref match-list 0))
  )


;; MAIN 
(define text (file-read))
(define r-pat (regex-pattern-maker))
(define ext-module (regex-lazy-eval r-pat text))
(display ext-module)

(newline)







