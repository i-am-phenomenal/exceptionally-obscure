#lang racket

(define invalid
    "NOT A PROPER STRUCTURE")

(cons (quote -) (cdr (quote (+ b c))))
(cdr (quote (+ b c)))
(cons 'd (cdr( cdr '(a b c d e f))))

(define (dummy_function argument)
  (let ((x argument))
     (+ argument 2)))

(let ((x 1))
  (let ((x 4))
    (display x))(display x))

(let ((b 1))
  (let ((a 1))
    (+ (+ (* 3 a) b) (-(* a 3) b))))

(let ((list_variable (list 1 2 3)))
   (cons (car list_variable) (cdr list_variable)))

(define (dumb argument)
  (display argument)
  (lambda (variable) (* variable variable) argument)
  )

(define square
  (lambda (operator num)
    (operator num num)))

(define single_argument_doubler
  (lambda (variable)
    (lambda (var)(variable var var))))

(define doubler
  (lambda (f)
    (lambda (x) (f x x))))

(define double_any
  (lambda (f x)
    ((doubler f)x)))


(define compose_cadr
  (lambda (argument)
      (car(cdr argument))))


(define compose_caar
  (lambda (argument)
    (if (list?(car argument))
        (car (car argument))
        "FIRST ELEMENT IS NOT A LIST")))

(define compose_cdar
  (lambda (argument)
    (if (list? (car argument))
        (cdr (car argument))
        "FIRST ELEMENT NOT A LIST")))


(define compose_caaar
  (lambda (argument)
    (if (list? (car argument))
        (car
         (if (list? (car (car argument)))
             (car (car argument))invalid))invalid)))

(define compose_caadr
  (lambda (argument)
    (if (list? (cdr argument))
        (car
         (if (list? (car (cdr argument)))
             (car (cdr argument))
             invalid))
        invalid)))

(define calculate
  (lambda (income)
    (cond
      ((<= income 10000)
       (* income 0.05))
      ((<= income 20000)
       (+ (* (- income 10000) 0.08) 500))
      ((<= income 30000)
       (+ (* ( - income 20000) 0.13) 1300))
      (else
       income))))

(define atom
  (lambda (argument)
    (if (pair? argument)
        "T"
        "F")))

(define shorter
  (lambda (argument1 argument2)
    (if (< (length argument1) (length argument2))
        argument1
        argument2)))


(define compose_length
  (lambda (argument)
    (if (null? argument)
        0
        (+ (compose_length (cdr argument))1))))



  (lambda (argument)
    ((if (null? argument)
             (cons '())
            (cons (car argument)(compose_list (cdr argument))))))

(define compose_list_v1
  (lambda (xs)
    (cond ((null? xs) '())
          ((null? (cdr xs)) (cons (car xs) null))
          (else (cons (car xs) (compose_list_v1 (cdr xs)))))))
          

(define compose_list
  (lambda (argument)
    (if (null? argument)
        (cons (car argument) null)
        (cons (car argument) (compose_list (cdr argument))))))

(define compose_first_car
  (lambda (element list_arg)
    (cond
      ((null? list_arg ) #f) 
      ((eq? (car list_arg) element) list_arg)
      (else
       (compose_first_car element (cdr list_arg))))))


(define remove_occurences
  (lambda (element argument)
    (cond
      ((null? argument) null)
      ((eq? (car argument) element) (remove_occurences element (cdr argument)))
      (else
        (cons (car argument) (remove_occurences element (cdr argument)))))))

(define make_list
  (lambda (n object)
     (cons object
      (cond
        ((= n 1) null)
        (else  (make_list (- n 1) object))))))
