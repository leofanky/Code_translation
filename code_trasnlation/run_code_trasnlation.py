import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          #frequency_penalty=0.1,
          max_tokens=500)

gpt.add_example(Example('Swift:\nprint("Hello, world!")', 'Kotlin:\nprintln("Hello, world!")'))
gpt.add_example(Example('Swift:\nvar myVariable = 42\nmyVariable = 50\nlet myConstant = 42', 'Kotlin:\nvar myVariable = 42\nmyVariable = 50\nval myConstant = 42'))
gpt.add_example(Example('Swift:\nlet explicitDouble: Double = 70', 'Kotlin:\nval explicitDouble: Double = 70.0'))
gpt.add_example(Example('Swift:\nlet label = \"The width is \"\nlet width = 94\nlet widthLabel = label + String(width)', 'Kotlin:\nval label = \"The width is \"\nval width = 94\nval widthLabel = label + width'))
gpt.add_example(Example('Swift:\nlet apples = 3\nlet oranges = 5\nlet fruitSummary = \"I have \(apples + oranges)\" + \"pieces of fruit.\"', 'Kotlin:\nval apples = 3\nval oranges = 5\nval fruitSummary = \"I have ${apples + oranges}\" + \"pieces of fruit.\"'))
gpt.add_example(Example('Swift:\nlet names = [\"Anna\", \"Alex\", \"Brian\", \"Jack\"]\nlet count = names.count\nfor i in 0..<count {\n\tprint(\"Person \(i + 1) is called \(names[i])\")}', 'Kotlin:\nval names = arrayOf(\"Anna\", \"Alex\", \"Brian\", \"Jack\")\nval count = names.count()\nfor (i in 0..count - 1) {\n\tprintln(\"Person ${i + 1} is called ${names[i]}\")}'))
gpt.add_example(Example('Swift:\nvar shoppingList = [\"catfish\", \"water\", \"tulips\", \"blue paint\"]\nshoppingList[1] = "bottle of water"', 'Kotlin:\nval shoppingList = arrayOf(\"catfish\", \"water\", \"tulips\", \"blue paint\")\nshoppingList[1] = "bottle of water"'))
gpt.add_example(Example('Swift:\nlet emptyArray = [String]()\nlet emptyDictionary = [String: Float]()', 'Kotlin:\nval emptyArray = arrayOf<String>()\nval emptyMap = mapOf<String, Float>()'))
gpt.add_example(Example('Swift:\nfunc greet(_ name: String,_ day: String) -> String {\n\treturn \"Hello \(name), today is \(day).\"\n}\ngreet(\"Bob\", \"Tuesday\")', 'Kotlin:\nfun greet(name: String, day: String): String {\n\treturn \"Hello $name, today is $day.\"\n}\ngreet(\"Bob\", \"Tuesday\")'))
gpt.add_example(Example('Swift:\nfunc getGasPrices() -> (Double, Double, Double) {\n\treturn (3.59, 3.69, 3.79)\n}', 'Kotlin:\ndata class GasPrices(val a: Double, val b: Double,\n\tval c: Double)\nfun getGasPrices() = GasPrices(3.59, 3.69, 3.79)'))
gpt.add_example(Example('Swift:\nlet numbers = [20, 19, 7, 12]\nnumbers.map { 3 * $0 }', 'Kotlin:\nval numbers = listOf(20, 19, 7, 12)\nnumbers.map { 3 * it }'))
gpt.add_example(Example('Swift:\nvar mutableArray = [1, 5, 3, 12, 2]\nmutableArray.sort()', 'Kotlin:\nlistOf(1, 5, 3, 12, 2).sorted()'))
gpt.add_example(Example('Swift:\nclass Shape {\n\tvar numberOfSides = 0\n\tfunc simpleDescription() -> String {\n\t\treturn \"A shape with \(numberOfSides) sides.\"\n\t}\n}\nvar shape = Shape()\nshape.numberOfSides = 7\nvar shapeDescription = shape.simpleDescription()', 'Kotlin:\nclass Shape {\n\tvar numberOfSides = 0\n\tfun simpleDescription() =\n\t\t\"A shape with $numberOfSides sides.\"\n}\nvar shape = Shape()\nshape.numberOfSides = 7\nvar shapeDescription = shape.simpleDescription()'))
gpt.add_example(Example('Swift:\nprotocol Nameable {\n\n\tfunc name() -> String\n}\nfunc f<T: Nameable>(x: T) {\n\tprint("Name is " + x.name())\n}', 'Kotlin:\ninterface Nameable {\n\tfun name(): String\n}\nfun f<T: Nameable>(x: T) {\n\tprintln(\"Name is \" + x.name())\n}'))
gpt.add_example(Example('Swift:\nextension Double {\n\tvar km: Double { return self * 1_000.0 }\n\tvar m: Double { return self }\n\tvar cm: Double { return self / 100.0 }\n\tvar mm: Double { return self / 1_000.0 }\n\tvar ft: Double { return self / 3.28084 }\n}\nlet oneInch = 25.4.mm\nprint(\"One inch is \(oneInch) meters\")\nlet threeFeet = 3.ft\nprint(\"Three feet is \(threeFeet) meters\")', 'Kotlin:\nval Double.km: Double get() = this * 1000\nval Double.m: Double get() = this\nval Double.cm: Double get() = this / 100\nval Double.mm: Double get() = this / 1000\nval Double.ft: Double get() = this / 3.28084\nval oneInch = 25.4.mm\nprintln("One inch is $oneInch meters")\nval threeFeet = 3.0.ft\nprintln("Three feet is $threeFeet meters")'))

### ---------------------------------------------- 
# gpt.add_example(Example('Kotlin:\nprintln("Hello, world!")', 'Swift:\nprint("Hello, world!")'))
# gpt.add_example(Example('Kotlin:\nvar myVariable = 42\nmyVariable = 50\nval myConstant = 42','Swift:\nvar myVariable = 42\nmyVariable = 50\nlet myConstant = 42'))
# gpt.add_example(Example('Kotlin:\nval explicitDouble: Double = 70.0', 'Swift:\nlet explicitDouble: Double = 70'))
# gpt.add_example(Example('Kotlin:\nval label = \"The width is \"\nval width = 94\nval widthLabel = label + width', 'Swift:\nlet label = \"The width is \"\nlet width = 94\nlet widthLabel = label + String(width)'))
# gpt.add_example(Example('Kotlin:\nval apples = 3\nval oranges = 5\nval fruitSummary = \"I have ${apples + oranges}\" + \"pieces of fruit.\"', 'Swift:\nlet apples = 3\nlet oranges = 5\nlet fruitSummary = \"I have \(apples + oranges)\" + \"pieces of fruit.\"'))
# gpt.add_example(Example('Kotlin:\nval names = arrayOf(\"Anna\", \"Alex\", \"Brian\", \"Jack\")\nval count = names.count()\nfor (i in 0..count - 1) {\n\tprintln(\"Person ${i + 1} is called ${names[i]}\")}', 'Swift:\nlet names = [\"Anna\", \"Alex\", \"Brian\", \"Jack\"]\nlet count = names.count\nfor i in 0..<count {\n\tprint(\"Person \(i + 1) is called \(names[i])\")}'))
# gpt.add_example(Example('Kotlin:\nval shoppingList = arrayOf(\"catfish\", \"water\", \"tulips\", \"blue paint\")\nshoppingList[1] = "bottle of water"', 'Swift:\nvar shoppingList = [\"catfish\", \"water\", \"tulips\", \"blue paint\"]\nshoppingList[1] = "bottle of water"'))
# gpt.add_example(Example('Kotlin:\nval emptyArray = arrayOf<String>()\nval emptyMap = mapOf<String, Float>()', 'Swift:\nlet emptyArray = [String]()\nlet emptyDictionary = [String: Float]()'))
# gpt.add_example(Example('Kotlin:\nfun greet(name: String, day: String): String {\n\treturn \"Hello $name, today is $day.\"\n}\ngreet(\"Bob\", \"Tuesday\")','Swift:\nfunc greet(_ name: String,_ day: String) -> String {\n\treturn \"Hello \(name), today is \(day).\"\n}\ngreet(\"Bob\", \"Tuesday\")'))
# gpt.add_example(Example('Kotlin:\ndata class GasPrices(val a: Double, val b: Double,\n\tval c: Double)\nfun getGasPrices() = GasPrices(3.59, 3.69, 3.79)', 'Swift:\nfunc getGasPrices() -> (Double, Double, Double) {\n\treturn (3.59, 3.69, 3.79)\n}'))
# gpt.add_example(Example('Kotlin:\nval numbers = listOf(20, 19, 7, 12)\nnumbers.map { 3 * it }', 'Swift:\nlet numbers = [20, 19, 7, 12]\nnumbers.map { 3 * $0 }'))
# gpt.add_example(Example('Kotlin:\nlistOf(1, 5, 3, 12, 2).sorted()', 'Swift:\nvar mutableArray = [1, 5, 3, 12, 2]\nmutableArray.sort()'))
# gpt.add_example(Example('Kotlin:\nclass Shape {\n\tvar numberOfSides = 0\n\tfun simpleDescription() =\n\t\t\"A shape with $numberOfSides sides.\"\n}\nvar shape = Shape()\nshape.numberOfSides = 7\nvar shapeDescription = shape.simpleDescription()', 'Swift:\nclass Shape {\n\tvar numberOfSides = 0\n\tfunc simpleDescription() -> String {\n\t\treturn \"A shape with \(numberOfSides) sides.\"\n\t}\n}\nvar shape = Shape()\nshape.numberOfSides = 7\nvar shapeDescription = shape.simpleDescription()'))
# gpt.add_example(Example('Kotlin:\ninterface Nameable {\n\tfun name(): String\n}\nfun f<T: Nameable>(x: T) {\n\tprintln(\"Name is \" + x.name())\n}','Swift:\nprotocol Nameable {\n\n\tfunc name() -> String\n}\nfunc f<T: Nameable>(x: T) {\n\tprint("Name is " + x.name())\n}'))
# gpt.add_example(Example('Kotlin:\nval Double.km: Double get() = this * 1000\nval Double.m: Double get() = this\nval Double.cm: Double get() = this / 100\nval Double.mm: Double get() = this / 1000\nval Double.ft: Double get() = this / 3.28084\nval oneInch = 25.4.mm\nprintln("One inch is $oneInch meters")\nval threeFeet = 3.0.ft\nprintln("Three feet is $threeFeet meters")','Swift:\nextension Double {\n\tvar km: Double { return self * 1_000.0 }\n\tvar m: Double { return self }\n\tvar cm: Double { return self / 100.0 }\n\tvar mm: Double { return self / 1_000.0 }\n\tvar ft: Double { return self / 3.28084 }\n}\nlet oneInch = 25.4.mm\nprint(\"One inch is \(oneInch) meters\")\nlet threeFeet = 3.ft\nprint(\"Three feet is \(threeFeet) meters\")'))


#       \t                    Tab
#       \\                    Inserts a back slash (\)
#        \'                    Inserts a single quote (')
#        \"                    Inserts a double quote (")
#        \n                    Inserts a ASCII Linefeed (a new line)
# Define UI configuration
config = UIConfig(description="Translate your code here",                   #top text
                  button_text="do it!",                                     #text on button
                  placeholder="Swift:\nprint('Hello, world!'')")            #example 

demo_web_app(gpt, config)

