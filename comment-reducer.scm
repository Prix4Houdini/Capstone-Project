(define module (comment-reducer))

(define (find-comment-range text st-index)
  ;;PROCEDURE DEFINITIONS
  (define (find-slash st-idx)
    (string-index text #\/ st-idx))

  (define (next-asterisk? st-idx)
    (string= "*" (substring text (+ st-idx 1) (+ st-idx 2))))

  (define (prev-asterisk? st-idx)
    (string= "*" (substring text (- st-idx 1) st-idx)))

  (define (no-more-comments? st-idx)
    (equal? #f st-idx))
  
  ;;PROCEDURE   
  (define a (find-slash st-index))  
  (cond ( (no-more-comments? a)
	  a)
	
	( (next-asterisk? a)
	  (let (
		(temp (find-slash (+ a 1)))
		)
	    (cond ((prev-asterisk? temp)
		   (list a (+ temp 1)))
		  )
	    ))
	
	( (equal? #t #t)
	  (list a (string-index text #\newline a)))
	)
  )
		   

(define-public (remove-comments-iter op_text ip_text st)
  ;; PROCEDURE DEFINITIONS
  (define (extract-till end)
    (substring ip_text st end))
  
  (define (extract-till-end)
    (substring ip_text st))
  
  ;; get start and end indices of comment
  (define char-range (find-comment-range ip_text st))
  (if (equal? #f char-range)
      
      (string-append op_text (extract-till-end))

      (let (
	    (temp (string-append op_text (extract-till (list-ref char-range 0))))
	    )
	
	    (remove-comments-iter temp ip_text (list-ref char-range 1))
	    ))
  )
       
      
