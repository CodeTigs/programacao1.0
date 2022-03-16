segundos = int(input());

minutos = int(segundos/60);
segundos -= minutos*60;
hrs = int(minutos/60);
minutos -= hrs*60;

print(repr(hrs)+":"+repr(minutos)+":"+repr(segundos))