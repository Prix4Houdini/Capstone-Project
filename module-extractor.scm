#!/usr/local/bin/guile -s
!#

(use-modules (ice-9 textual-ports))
(use-modules (ice-9 regex))

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
	(regex-iter pattern temp-string "") ; else call regex-iter
	)
    )
  )

;; proceedure to match regex with text
(define (match-regex pattern t-string)
  (define match-list (map match:substring (list-matches pattern t-string)))
  (if (= (length match-list) 0) "" (list-ref match-list 0))
  )


;;; core tail-recursive function of regex lazy evaluation
(define (regex-iter pattern matched-text initial-text)
  ;; DEFINITIONS OF LOCAL PROCEEDURES
  ;; removes the characters 'endmodule' from the end of the text using indices to slice the string
  (define (remove-endmodule)
    (define new_len (- (string-length matched-text) 9))
    (substring matched-text 0 new_len)
    )

  ;; PROCEEDURE
  ;; if matched-text is an empty string
  (if (string= "" matched-text)
      initial-text   ; if condition is true - termination condition
      
      ;; else call regex-iter once again
      (let ( (temp-string (match-regex pattern (remove-endmodule))))
	(regex-iter pattern temp-string matched-text) ; call regex-iter tail-recursively
      ))
  )


;; MAIN 
(define text (file-read))
(define r-pat (regex-pattern-maker))
(define ext-module (regex-lazy-eval r-pat text))
(display ext-module)



(newline)







