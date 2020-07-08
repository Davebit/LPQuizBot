grammar Enquestes;

root : (expr)* 'END';

expr: (pregunta | resposta | item | alternativa | enquesta) ;

pregunta: ID ':' 'PREGUNTA' TEXT*;
resposta: ID ':' 'RESPOSTA'   opcio* ;
item: ID ':' 'ITEM' assig ;
alternativa: ID ':' 'ALTERNATIVA' ID '[' alt ']';
enquesta: ID ':' 'ENQUESTA' ID* ;

opcio: NUMBER ':' TEXT* ';' ;

assig: ID '->' ID ;

alt: new (',' new)* ;
new: '(' NUMBER ',' ID ')' ;

ID : [A-Z][0-9]*;
NUMBER : [0-9]+ ;
TEXT : [a-zA-Z?\u0080-\u00FF]+ ;
WS : [ \t\r\n\f]+ -> skip;