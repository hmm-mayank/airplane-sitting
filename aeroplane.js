

let assigned = [
    [3, 2],
    [4, 3],
    [2, 3],
    [3, 4],
  ];
  
  let totalNumberSeat = 30;
  
  const allocateSeat = (seatSet,currentSeat,seatInRow)=> {
let r='';
    for (i=1;i<=seatInRow;i++) {

        r+=" "+i+""+currentSeat+""+seatSet;
    }
    console.log(r)
  }
  const totalSeats = (arr) => arr.reduce( (a, b) => a * b );
const repeatSeat = (j,rep,totalElemmet,id) => {


let r = ''
allocateSeat(id,j,rep)
    return r;
}

let magic = "";
let newLine = "";
let totalOcupency = 0;
assigned.forEach((element,id) => {
totalOcupency+=totalSeats(element);
  for (let j = 0; j < element[1]; j++) {
    let getSitting = ` ${repeatSeat(j,element[0],element,id)}`;
    magic += `${getSitting}`;
  }
  console.log(magic);
  magic = "";
});


console.log("TOTAL SEATS IN AEROPLANE "+totalOcupency)
