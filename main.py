import 'dart:async';
import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:sample/fetching_input.dart';
void main() {
  runApp(myCalculator());
}

class myCalculator extends StatelessWidget{
  const myCalculator({Key? key}) : super(key:key);
  @override

  Widget build(BuildContext context){
    return MaterialApp(
      home: introduction(),
    );
  }
}



class introduction extends StatefulWidget{
  @override
  State<StatefulWidget> createState() => InputPage();
}


class InputPage extends State<introduction>{
  Color _colors=Colors.red;


  var textinput=TextEditingController();
  var types;
  RangeValues values =RangeValues(0, 100);
  double index=500;

   void MAINFUCNTION(double value){
        setState(() {
          index=value;
          _colors=Colors.green[value.toInt()]!;
});

  }

  @override
  Widget build(BuildContext context) {
    RangeLabels labels = RangeLabels(
        values.start.toString(), values.end.toString());

    return Scaffold(
        appBar: AppBar(
          title: Center(child: Text("Input Page")),

        ),
        body: Column(
          children: [
            Slider(
              value: index.toDouble(),
              label: "${index.round()}",
              divisions: 10,

              activeColor: Colors.red,
              min: 0,
              max: 1000,
              onChanged: MAINFUCNTION

            ),
      TextField(
        controller: textinput,
      )
      ,
          ElevatedButton(onPressed: (){


            print(textinput.text);
      },
          child: Text("button")),

          Container(
            color: _colors,

            width: 200,
            height: 200,
      )
          ],
        )
    );
  }
}
