valor  =  eval ( entrada ())

cem  =  cinquenta  =  vinte  =  dez  =  cinco  =  dois  =  um  =  0
cincents  =  vintecincents  =  dezcents  =  cincocents  =  centavos  =  0

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 100 ) > =  1 :
	cem  =  int ( valor / 100 )
	valor  - =  cem * 100 ;

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 50 ) > =  1 :
	cinquenta  =  int ( valor / 50 )
	valor  - =  cinquenta * 50

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 20 ) > =  1 :
	vinte  =  int ( valor / 20,00 )
	valor  - =  vinte * 20 ;

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 10 ) > =  1 :
	dez  =  int ( valor / 10 )
	valor  - =  dez * 10,00

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 5 ) > =  1 :
	cinco  =  int ( valor / 5 )
	valor  - =  cinco * 5

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 2 ) > =  1 :
	dois  =  int ( valor / 2 )
	valor  - =  dois * 2

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 1 ) > =  1 :
	um  =  int ( valor / 1 )
	valor - =  um * 1

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 0,50 ) > =  1 :
	centavos  =  int ( valor / 0,50 )
	valor  - =  centavos * 0,50

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 0,25 ) > =  1 :
	vintecincents  =  int ( valor / 0,25 )
	valor  - =  vintecincents * 0,25 ;

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 0,10 ) > =  1 :
	dezcents  =  int ( valor / 0,10 )
	valor  - =  dezcents * 0,10 ;

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 0,05 ) > =  1 :
	cincocents  =  int ( valor / 0,05 )
	valor  - =  cincocents * 0,05 ;

value  =  float ( "% .2f"  %  valor )
se  int ( valor / 0,01 ) > =  0,998 :
	centavos  =  int ( valor / 0,01 )
	valor  - =  centavos * 0,01 ;

imprimir ( "NOTAS:" )
imprimir ( "% d nota (s) de R $ 100,00"  %  cem )
imprimir ( "% d nota (s) de R $ 50,00"  %  cinquenta )
print ( "% d nota (s) de R $ 20,00"  %  vinte )
print ( "% d nota (s) de R $ 10,00"  %  dez )
imprimir ( "% d nota (s) de R $ 5,00"  %  cinco )
imprimir ( "% d nota (s) de R $ 2,00"  %  dois )

imprimir ( "MOEDAS:" );
imprimir ( "% d moeda (s) de R $ 1,00"  %  um );
imprimir ( "% d moeda (s) de R $ 0,50"  %  centavos )
imprimir ( "% d moeda (s) de R $ 0,25"  %  vintecentes )
imprimir ( "% d moeda (s) de R $ 0,10"  %  dezcents )
imprimir ( "% d moeda (s) de R $ 0,05"  %  centavos )
imprimir ( "% d moeda (s) de R $ 0,01"  %  centavos )