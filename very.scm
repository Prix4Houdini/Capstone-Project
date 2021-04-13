#!/usr/local/bin/guile -s
!#

(use-modules (ice-9 textual-ports))
(use-modules (ice-9 regex))

(define (file-read)
  ;; read command line arguments
  (let ( (verilog-file (list-ref (command-line) 1)) )
    ;; return file to calling proceedure
    (
     let ( (file (open-input-file verilog-file)) )
      (get-string-all file)
      )
    )
  )

(define (regex-pattern-maker)
    (let ((module-start "module[[:space:]]")
	  (verilog-module (list-ref (command-line) 2))
	  (body "((.|\n)*)?")
	  (endmodule "endmodule"))
		  
      (string-append module-start verilog-module body endmodule))
    )
 
;;; implementation of lazy evaluation for regex matching
;(define (regex-lazy-eval pattern source-text)
  ;; apply pattern on source-text
  ;; if patternized output is empty string, then return error
  ;; else call regex-iter
 ; )


;;; core tail-recursive function of regex lazy evaluation
(define (regex-iter pattern matched-text initial-text)
  ;; DEFINITIONS OF LOCAL PROCEEDURES
  ;; removes the characters 'endmodule' from the end of the text using indices to slice the string
  (define (remove-endmodule)
    (define new_len (- (string-length matched-text) 9))
    (substring matched-text 0 new_len)
    )
  ;; proceedure to match regex with text
  (define (match-regex t-string)
    (define match-list (map match:substring (list-matches pattern t-string)))
    (if (= (length match-list) 0) "" (list-ref match-list 0))
    )

  ;; PROCEEDURE
  ;; if matched-text is an empty string
  (if (string= "" matched-text)
      initial-text   ; if condition is true - termination condition
      
      ;; else call regex-iter once again
      (let ( (temp-string (match-regex (remove-endmodule))))
	(regex-iter pattern temp-string matched-text) ; call regex-iter tail-recursively
      ))
  )
 
(define temp (file-read))
(define tepm (regex-pattern-maker))



(newline)







