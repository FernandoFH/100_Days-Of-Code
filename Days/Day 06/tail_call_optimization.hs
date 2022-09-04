-- tail call optimizacion

sumaTotal x = if x == 0 
    then 0
    else x + sumaTotal (x-1)

sumaTotalOps x  y = if x == 0 
    then y
    else sumaTotalOps (x-1) (x+y)