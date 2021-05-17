; syntax macros

(define (printer arg)
  (display (string-append (symbol->string arg) "\n")))

(define-syntax module
  (syntax-rules (endmodule)
    ((_ module-name body)
     (printer (quote module-name)))))


;(define-syntax module
;  (syntax-rules (endmodule)
;    ((_ module-name body)
;     ((printer (quote module-name))
;      (printer (quote body))))))

; test input
; (module booth a)


(define-syntax module
  (syntax-rules (endmodule)
    ((_ module-name args body endmodule)
     (list (quote module-name) (quote args) (quote body) (quote endmodule)))))

;; Next tries

(define-syntax lx
  (syntax-rules ()
    ((_ module_name (. args)#\; body endmodule)
     (quote args))))

(lx booth (input wire x1, input wire x2)#\; body endmodule)

;;; almost done

(define-syntax lx
  (syntax-rules ()
    ((_ module-name (. args)#\; exp ... endmodule-token)
     (quote (exp ...)))))

;;; version 1

(define-syntax module
  (syntax-rules ()
    ((_ module-name (. args)#\; exp ... endmodule)
     (list (quote args) (quote (exp ...))))))

;; test case
(module booth (input wire x1, input wire x2)#\; body body2 body3 endmodule)
