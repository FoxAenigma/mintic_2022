public class Computadores{
    //Constants
    public final static int PESO_BASE=5;
    public final static char CONSUMO_W_BASE='F';
    public final static double PRECIO_BASE=100;

    //Atributes
    public int peso;
    public char consumoW;
    public double precio;

    //Constructors
    public Computadores(){
        this.precio=PRECIO_BASE;
        this.peso=PESO_BASE;
        this.consumoW=CONSUMO_W_BASE;
    }

    public Computadores(double precio, int peso){
        this.precio=precio;
        this.peso=peso;
        this.consumoW=CONSUMO_W_BASE;
    }

    public Computadores(double precio, int peso, char consumoW){
        this.precio=precio;
        this.peso=peso;
        this.consumoW=consumoW;
    }

    //Methods
    public double calcularPrecio(){
        double totalUnidad=this.precio;

        //Power adition
        switch(this.consumoW){
            case 'A':
                totalUnidad+=100;
                break;
            case 'B':
                totalUnidad+=80;
                break;
            case 'C':
                totalUnidad+=60;
                break;
            case 'D':
                totalUnidad+=50;
                break;
            case 'E':
                totalUnidad+=30;
                break;
            case 'F':
                totalUnidad+=10;
                break;
            default:
                break;
        }

        //Weigth adition
        if(this.peso>=0 && this.peso<19){
            totalUnidad+=10;
        } else if (this.peso>=20 && this.peso<49){
            totalUnidad+=50;
        } else if (this.peso>=50 && this.peso<=79){
            totalUnidad+=80;
        } else if (this.peso>=80) {
            totalUnidad+=100;
        }

        return totalUnidad;
    }
        //MAIN
        public static void main(String[] args){
         	
            Computadores computadores[] = new Computadores[6];
            computadores[0] = new Computadores(150.0, 70, 'A');
            computadores[1] = new ComputadoresMesa(70.0, 40);
            computadores[2] = new ComputadoresPortatiles(600.0, 70, 'D', 50, false);
            computadores[3] = new Computadores();
            computadores[4] = new Computadores(500.0, 60, 'A');
            computadores[5] = new Computadores(700.0, 50, 'D');
            PrecioTotal solucion1 = new PrecioTotal(computadores);
            solucion1.mostrarTotales();
            System.out.println();
        }
}

class ComputadoresMesa extends Computadores{
    //Constans
    public final static int ALMACENAMIENTO_BASE=50;

    //Atributes
    public int almacenamiento;

    //Constructors
    public ComputadoresMesa(){
        this.almacenamiento=ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(double precio, int peso){
        super(precio, peso);
        this.almacenamiento=ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(double precio, int peso, char consumoW, int almacenamiento){
        super(precio, peso, consumoW);
        this.almacenamiento=almacenamiento;
    }

    //Methods
    public double calcularPrecio(){
        double totalUnidad = super.calcularPrecio();

        if (this.almacenamiento > 100){
            totalUnidad+=50;
        }

        return totalUnidad;
    }
}

class ComputadoresPortatiles extends Computadores{
    //Constansts
    public final static int PULGADAS_BASE=20;
    public final static boolean CAMARA_BASE=false;

    //Atributes
    public int pulgadas;
    public boolean camaraITG;

    //constructors
    public ComputadoresPortatiles(){
        this.pulgadas=PULGADAS_BASE;
        this.camaraITG=CAMARA_BASE;
    }

    public ComputadoresPortatiles(double precio, int peso){
        super(precio, peso);
        this.pulgadas=PULGADAS_BASE;
        this.camaraITG=CAMARA_BASE;
    }

    public ComputadoresPortatiles(double precio, int peso, char consumoW, int pulgadas, boolean camaraITG){
        super(precio, peso, consumoW);
        this.pulgadas=pulgadas;
        this.camaraITG=camaraITG; 
    }

    //Methods
    public double calcularPrecio(){
        double totalUnidad = super.calcularPrecio();

        //Size adition
        if (this.pulgadas>40){
            totalUnidad+=0.3*this.precio;
        }

        //Camera verification
        if (this.camaraITG){
            totalUnidad+=50;
        }

        return totalUnidad;
    }
}

class PrecioTotal{
    //Atributes
    public double totalComputadores;
    public double totalMesa;
    public double totalPortatiles;
    public Computadores[] listaComputadores;

    //Constructor
    public PrecioTotal(Computadores[] listaComputadores){
        this.listaComputadores=listaComputadores;
    }
    
    //Methods
    public void mostrarTotales(){
        for(int i=0; i<listaComputadores.length; i++){
      
            if(listaComputadores[i] instanceof Computadores){
                totalComputadores+=listaComputadores[i].calcularPrecio();
            }
            if(listaComputadores[i] instanceof ComputadoresMesa){
                totalMesa+=listaComputadores[i].calcularPrecio();
            } 
            if(listaComputadores[i] instanceof ComputadoresPortatiles){
                totalPortatiles+=listaComputadores[i].calcularPrecio();
            }
        }

        System.out.println(String.format("La suma del precio de los computadores es de %.1f", totalComputadores));
        System.out.println(String.format("La suma del precio de los computadores de mesa es de %.1f", totalMesa));
        System.out.println(String.format("La suma del precio de los computadores portátiles es de %.1f", totalPortatiles));
    }
}
