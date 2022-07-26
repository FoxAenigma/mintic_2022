import java.lang.Math;

public class BecaUniversitaria{
    double period;
    double capital;
    double rate;

    public BecaUniversitaria(double ... vars){
        if(vars.length!=0){
            this.period=vars[0];
            this.capital=vars[1];
            this.rate=vars[2];
        }
    }

    public double calcularInteresSimple(){
        return Math.round((this.capital*this.rate/100)*this.period);
    }
    public double calcularInteresCompuesto(){
        return Math.round(this.capital*(Math.pow(1+this.rate/100,this.period)-1));
    }
    public String compararInversion(double ... vars){
        if(vars.length!=0){
            this.period=vars[0];
            this.capital=vars[1];
            this.rate=vars[2];
        }
        double diff=this.calcularInteresCompuesto()-this.calcularInteresSimple();
        String flag;
        if(diff!=0){flag=String.format("La diferencia entre la proyección de interés compuesto e interés simple es: $%.1f",diff);}
        else{flag="No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";}
        return flag;
    }
}