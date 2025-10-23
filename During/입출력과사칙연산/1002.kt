import java.util.* 
import kotlin.math.* 

val X=0; val Y=1; val R=2;
    
fun SameTest<Int> (a:MutableList, b:MutableList){
    var same:Int = 0
    for (i in x..r+1){
        if(xyr1.get(i) == xyr2.get(i)){
            same++
        }
    }
    return same
}

fun Point<Int>(a:MutableList,b:MutableList) {
    var ax:Int = a.get(X)
    var ay:Int = a.get(Y)
    var ar:Int = a.get(R)
    var bx:Int = b.get(X)
    var by:Int = b.get(Y)
    var br:Int = b.get(R)
    
    var range:Int = sqrt(ax*ax + bx*bx)
    if (range== ar+br) {
        return 1
    } else { return 2 }
    return 0
}

fun main() {
    val sc: Scanner = Scanner(System.`in`)
    val xyr1 = mutableListOf<String>()
    val xyr2 = mutableListOf<String>()
    for(i in 0..6) {
        var temp = sc.nextInt()
        if(i<3){xyr1.add(temp)
        } else { xyr2.add(temp) }
    }
    if (SameTest(xyr1,xyr2)==3){println("-1")}
    else { println(Point(xyr1, xyr2)) }
    
    return 0
}