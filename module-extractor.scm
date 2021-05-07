#!/usr/local/bin/guile -s
!#

(use-modules (ice-9 textual-ports))
(use-modules (ice-9 regex))

;; MODULE EXTRACTOR
(define (file-read)
  (let* ((file-name    (list-ref (command-line) 1))  ; read verilog filename from command line arg
	 (file-handler (open-input-file file-name))) ; open file-handler
    (get-string-all file-handler))) ; read file  

(define (module-begin-pattern) ; create regex pattern for module beginning
    (let ((module-start "module[[:space:]]") 
	  (verilog-module (list-ref (command-line) 2)))	  
      (string-append module-start verilog-module))) 

(define (extractor pattern text) ; extract module from text file
  (define matched-string (string-match pattern text)) ; returns match object, else returns false
  (if (eq? #f matched-string)
      ""
      (let* ((st   (match:start matched-string)) ; get starting index from match object
	     (end (match:end   (string-match "endmodule" text st)))) ; index of endmodule
	(substring text st end)))) ; return substring
    
;; COMMENT ELIMINATOR
(define (find-comment-range text st-index)
  ;;PROCEDURE DEFINITIONS
  (define (find-slash st-idx)
    (string-index text #\/ st-idx))
  (define (next-asterisk? st-idx)
    (string= "*" (substring text (+ st-idx 1) (+ st-idx 2))))
  (define (prev-asterisk? st-idx)
    (string= "*" (substring text (- st-idx 1) st-idx)))
  
  ;;PROCEDURE   
  (define a (find-slash st-index))  
  (cond ((equal? #f a) a) ; return #f if there are no more comments
	((next-asterisk? a) ; if asterisk follows forward slash - multiline comments
	 (let ((temp (find-slash (+ a 1)))) ; find next slash
	   (cond ((prev-asterisk? temp)
		  (list a (+ temp 1)))))) ; return a list (a (+ temp 1))
					  ; haven't handled condition where previous is not asterisk
	(else (list a (string-index text #\newline a))))) ; single line comments
		   
(define (remove-comments-iter op_text ip_text st)
  ;; PROCEDURE DEFINITIONS
  (define (extract-till end)
    (substring ip_text st end))
  (define (extract-till-end)
    (substring ip_text st))
  
  ;; get start and end indices of comment
  (define char-range (find-comment-range ip_text st))
  (if (equal? #f char-range)
      (string-append op_text (extract-till-end)) ; return till the end of string if last comment
      (let ((temp (string-append op_text (extract-till (list-ref char-range 0)))))
	(remove-comments-iter temp ip_text (list-ref char-range 1))))) ; remove next comment


;; WRAPPER
(define (module-extractor)
  (let* ((ip  (file-read))
	(pat (module-begin-pattern))
	(int (extractor pat ip)))
    (remove-comments-iter "" int 0)))

;; MAIN 
(display (module-extractor))

(newline)







