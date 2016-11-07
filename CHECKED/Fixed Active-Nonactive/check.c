#include <stdio.h>

#define M 3
#define N 3
#define len 6


_Bool nondet_bool();
unsigned int nondet_uint();

typedef unsigned __CPROVER_bitvector[M] bitvector; 


unsigned int  nondet (){  
  unsigned int num = nondet_uint();
  __CPROVER_assume( num>= 0 && num  <= 1);
   return num;
};

unsigned int zeroTon(unsigned int n) {
    unsigned int result = nondet_uint();
    __CPROVER_assume(result >=0 && result <=n);
    return result ;
};

struct EdgeBag
 {
   unsigned int ith;
   unsigned int jth;
};

int  main()
 {    
	 
    unsigned int pos, i, j, k, l, m ,n ,w, x, y , z, e1,e2,e3, iVal, jVal, g, g0, gl, lastg, ng, nl, nl2 ;
    unsigned int edgePos = 0, bagNo = 0, colorNode = 0 , minColor, cPos = 0 , tComp, result;
    unsigned int  ticks, ticks2, valj, vali , calc, edgeCount = 0;
    _Bool Ck=0, Cl = 0,Cf = 1, C0 = 1, C1 = 1, C2 = 1, C3 = 1, C4, C5, C6 , C7; 
   
    bitvector Vnodes[N], Tnodes[N];
    bitvector  fareTotal, inTotal, outTotal , outVSnareTotal , inVSnareTotal , outTSnareTotal , inTSnareTotal ;
    
    unsigned int graph[N][N];
    

    for (i = 0; i < N; i++) {
       for (j = 0; j < N; j++) {
	      if(i != j) {
		      __CPROVER_assume(graph[i][j] >= 0 && graph[i][j] <=2);
	          if (graph[i][j] == 1) {
                 edgeCount += 1;	
		      }
              else if (graph[i][j] == 2) {
		         edgeCount += 2;
		      }
          }
          else  
		      __CPROVER_assume(graph[i][j] == 0); 
       } 
    }

   __CPROVER_assume(edgeCount == len);
     
   struct EdgeBag edgeBag[len];

     for  (i = 0; i < N; i++) {
             for  (j = 0; j < N; j++) {
               if ((graph[i][j] == 1) || (graph[i][j] == 2)) {
                   edgeBag[edgePos].ith = i;     // Record the source node
                   edgeBag[edgePos].jth = j;     // Record the target Node
 
                   edgePos = edgePos + 1;
             }
 
             if ((graph[i][j] == 2)) {
                  edgeBag[edgePos].ith = i;      // Record the Source Node  
                  edgeBag[edgePos].jth = j;      // Record the Target Node
                   edgePos = edgePos + 1;
             }

          }
     }
  
   C5 = 1;

  for (x = 0; x < len; x++) {
     for (y = (x + 1); y < len; y++) {
        for (z = (y + 1); z < len; z++) {
		  
		   unsigned int graph1[N][N];
           
           for (m=0;m<N;m++){
			  for (n=0;n<N;n++) {
		        graph1[m][n] = graph[m][n];
		      }
	        }
	         
	        graph1[edgeBag[x].ith][edgeBag[x].jth] = (graph1[edgeBag[x].ith][edgeBag[x].jth] - 1);
	        graph1[edgeBag[y].ith][edgeBag[y].jth] = (graph1[edgeBag[y].ith][edgeBag[y].jth] - 1);		     
	        graph1[edgeBag[z].ith][edgeBag[z].jth] = (graph1[edgeBag[z].ith][edgeBag[z].jth] - 1);
	         

          // STRONGLY CONNECTED
          for ( i = 0; i < N; i++) {
             for (j = 0; j < N ; j++) {
                if ( (i != j) && ((graph1[i][j] >= 1) || graph1[j][i] >= 1 )) {  // if there is Direct edge we are done
                    C5 = C5 && 1;
                }

                else if(i != j) {  // Else case
                    unsigned int nub;  // Define max hop
                    __CPROVER_assume( nub >= 1 && (nub <= N-2));
                    unsigned int gPath[nub];
                
                    for (k = 0; k < nub; k++) {   // zdynamic N - 2 iteration
                        gPath[k] = zeroTon(N-1);
                     }
                    //  Make sure first edge is connected to i  and last edge is connected to j
                    if( ((graph1[i][gPath[0]] >= 1) || (graph1[gPath[0]][i] >= 1)) 
                    && ((graph1[gPath[nub - 1]][j] >= 1) || (graph1[j][gPath[nub - 1]] >= 1))) {   
                        C5 = C5 && 1;
				    }
                    else  {
                        C5 = 0;
                    }
               // rest Of the case is just checking edge btw consecutive array elements
                 for (l = 0; l < nub - 1; l++) {         //Dynamic N - 3  iteration
                      if ( (graph1[gPath[l]][gPath[l+1]] >= 1 ) || (graph1[gPath[l+1]][gPath[l]] >= 1 )) { 
                               C5 = C5 && 1;
					   }
                      else {
                            C5 = 0;
					  }
                 }
                }   
            }
         }
         
        
         
      }
   }
}

  
    for(i = 0;i < N ; i++) {
        for( j = 0;j < N; j++) {
            printf("Graph[%d][%d] = %d",i,j,graph[i][j]);
        }
    }
    

  __CPROVER_assert(!C5, "Graph that satisfy friendZoned model exists");  
 
}

