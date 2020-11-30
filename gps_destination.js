d= 0.1;
R= 6371;
φ1 = 17;
λ1 = 78;
brng = 0;
const φ2 = Math.asin( Math.sin(φ1)*Math.cos(d/R) +
                      Math.cos(φ1)*Math.sin(d/R)*Math.cos(brng) );
const λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1),
                           Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));
console.log(φ2)
console.log(λ2)