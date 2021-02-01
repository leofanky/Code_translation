Introduction
- Importance of the Choice of the topic;
- Statement of the problem;
- Analytical Review of the state of the issue/ Literature Review;


Translation between the native languages of mobile development.
As we all know we use our mobiles everyday and for almost everything now, but we all don’t have the same phone, I’m mostly talking about the two main operating systems that are in the market, that utilizes both their own proprietary language. As the two main players of this space we encounter Google with Android and Apple with iOS, the languages being Kotling and Swift.






















Main differences between kotlin and swift.
Aside from the Syntactical Differences that you can see below: 






Optional and Nullable Types
Both Swift and Kotlin have put effort into ensuring devs don’t accidentally end up with the null pointer exceptions, both use a kind of wrapper type that lets you safely access the underlying values: Swift calls this type Optionals, Kotlin calls them nullables. All you need to do is set a ? after the variable type.
Kotlin nullable string when used in action prints the same string as a non-nullable type. Different from Swift, it doesn’t wrap itself in an optional wrapper. This difference is caused by the way Optionals are implemented in Swift as they’re essentially an enum.
Kotlin nullables contain a null type checker, which the compiler uses when the bytecode is generated to handle the null references.
In both a ? needs to be placed after the object for querying properties or calling functions. In Swift, this is called optional chaining, and in Kotlin, it’s called safe calls.
Swift has a nil-coalescing operator, ??, that safely unwrap a value if it exists or provides a default value when empty. In Kotlin, the same can be done using a ?: Elvis operator.
To handle Optionals properly and apply some additional operations on the unwrapped values, should use a null checker or smart cast ( is or as) in Kotlin. Swift, on the other hand, provides us with if let and guard let statements that are a lot more readable.
There’s no similar optional binding syntax for Kotlin, it does provide a let() lambda function that executes the action only when the value is non-nullable. But this is different from the if let and guard let approaches since it doesn’t let you access the local variable in the scope.
While neither recommend using force unwrapping or not-null assertion, the syntax for doing it is ! for Swift and !! for Kotlin.
Implicit wrapping in Swift indicates to the compiler to ignore the safe unwrap since the property would always have a value available. In Kotlin, the same is done by using the lateinit keyword in the variable declaration.
Both Kotlin and Swift allow safe casting using as? .



Control Flows
if-else, for, and switch are the basic control flow statements available in most languages.
In Swift, the parentheses around the condition aren’t necessary, but setting curly braces around the if-else condition is mandatory. Kotlin does just the opposite, similar to Java and lets you get away with curly braces in one-liner conditions, thereby posing ambiguity due to the dangling else problem.
Kotlin and Swift both have differed from C-style for loops and instead give more emphasis to for in loops. There is the ability  to create for loops using the range operator.
The until operator in Kotlin is analogous to ..< in Swift. Both exclude the last value. There’s an alternative way to increment or decrement values in the for loop iterations as well.
Swift presents us with a stride operator, which has two variants: 
stride(from:to:by:)		 (excludes the to value)
stride(from:through:by:)	 (includes the through value).
Kotlin provides us with step to control the increment and downTo for creating steps in reverse order.
Switch statement in Swift is equal to when in Kotlin. The Swift switch needs to be exhaustive, it isn’t necessary with Kotlin’s statement when (unless the statement is returning a value).
Both statements are incredibly powerful and offer pattern matching, multiple cases, and typecasting, for some examples. In Swift using a case let or range operators, you can do a partial match. Kotlin provides us with in (range of argument) and is (smart casting) operators while not letting you pass arguments in the when statement.


Classes, Functions, Constructors, and Inheritance
Basic declaration of classes and functions in both languages is almost the same, but there are some subtle differences.
The Kotlin classes, functions, and properties defined are final by default. Meaning that they can’t be inherited, to allow subclassing or overriding, we need to declare them as open class and open fun.
Swift functions support internal and external parameter names, improving the function’s readability. A variable number of arguments in Kotlin can be specified using:
fun sum(vararg numbers: Int),
and in Swift, the following signature is used: 
func sum(_ numbers: Int...).
Constructors are implemented in different ways. Kotlin lets you declare the primary constructor in the class header, with an option to set default values, secondary constructors are declared using the constructor keyword in the class body. If the class contains a primary constructor, the secondary constructor must refer to it using this. There’s an init block that runs whenever the class is initialized.
Constructor arguments are val by default, unless you specify them as var. As for subclasses in Kotlin, in case a primary constructor isn’t defined, the secondary constructor must use the super keyword to call the base class or delegate to another constructor that does that using this.
In Swift, the init block represents the primary constructor. It is a designated initializer that’s responsible for setting up all the properties of that class, Swift has a secondary initializer known as a convenience initializer, designates to the primary one by letting you assign default values to some properties.
Swift includes required and automatic-initializer inheritance. The required keyword set on any initializer it enforces you to implement that initializer in subclasses. Automatic-initializer inheritance follows two rules:
Don’t define any designated initializers in your subclass — they’ll be inherited automatically
Implement all the designated initializers of the base class. All the convenience initializers will be inherited implicitly.

Structs and Data Classes
Kotlin’s primary constructor syntax makes it easy to create a data class for storing data. But Kotlin doesn’t have a way to create a custom type for passing data by value, like structures in Swift.

Closures
Lambda expressions aren’t just functions without a name. Closures are a type of lambda that lets you capture values outside of the scope it’s defined in. The return type of a closure is specified after -> in both Swift and Kotlin. Kotlin provides an it parameter for single-value closures, and the -> can be escaped. Swift, on the contrary, lets you use $0, $1, $2, and so on.
While the Swift closures can be defined as escaping and non-escaping, Kotlin closures are escaping by default. This has a lot to do with the memory-management systems of the two languages: Swift uses Automatic Reference Counting and Kotlin uses the Garbage Collector.

Extensions
Extensions in Swift lets you add extra functionality to classes, structs, enums, and protocols without actually extending them. In Kotlin, extensions are more like static methods of Java.
Note: Kotlin provides get() and set(value) methods by default for all property declarations. Swift, on the other hand, makes use of a more flexible computed property syntax with get{} and set{} and the property observers didSet and willSet, which are triggered when the value is changed.

Interfaces and Protocols
Interfaces in Kotlin are known as protocols in Swift. Both are responsible for defining a set of functions or properties the class can conform to. The difference is Kotlin allows us to set default implementations in the interface. As a workaround for Swift, you can use extensions on the protocols.
Also for generics, Swift lets you define a associatedType in the protocol; whereas for Kotlin, you can use the generic type T in the definition.

Enumerations
Enumerations in Kotlin are a class that holds a bunch of constants with a custom data type. On the other hand, in Swift, enums are first-class citizens that let us specify the associated value of any type with every case. Kotlin Enums, on the other hand, can have only one object per type.
Now, Kotlin does have a workaround in the form of sealed classes, which let you create instances with different types. But again, sealed classes are a reference type which entirely replicates the Swift enums value type.


Lastly, lazy in Swift lets you defer the initialization of the property till first access. In Kotlin the same can be achieved using the delegated properties by feature. While with Swift, lazy is a keyword that’s applicable only to mutable properties, the by lazy accepts a lambda function and is applicable to only immutable properties (it can’t be changed once set).









There are some solutions out there, like the flutter sdk with dart language you can create apps that can run in both operating system ( you can see an example in my github: leofanky/convo (github.com) ) because the final code is compile in native code but the functionality is really limited still and is not fully developed yet as is still in beta stage in many aspects.
I found some project online trying to do a translation as an example: Gryphon, but it is only a preview and they don’t use ML or any other kind of new technologies but is more like a dictionary. 
Main issue in the market is for small to medium companies that face the challenge of choosing a platform as there aren’t many developers that code in both and furthermore they are really requested and with a really high salary. So the idea would be to take your native code being Kotlin or Swift and translating to the other.






















Main
-Description and justification of the Method;
-Presentation and analysis of the result;
-Analytical Comparison with already known result;


Why did I choose to use a ML algorithm for code translation? 
Not so long ago the public had no idea computers could generate code by themself until we started seeing big Tech companies that needed pipelines for automated testing and for code snippet generation for speeding up the process of coding and testing. But at the same time we see a big divide, especially in the mobile industry, there are the two big players that we all know and use at least one of them everyday, Google/Android and Apple/iOS. Both of them are already using a lot of ML to analyze behaviour and better apps and OS, also using for Database management and Management in general, so why not implement Machine Learning to the creation of such apps, so this is where my idea of using NLP (Natural Language Processing), that is a big part of ML, as we know iOS language (Swift) and Android language (kotlin) are high level languages, what does this mean? It means that they are easier to read, write, and maintain because they have a higher level of abstraction and as such they are human readable and have a similar structure to a human understandable language, meaning that programs written in a high-level language must be translated into machine language by a compiler or interpreter.
The best NLP algorithm known is GPT created by OpenAI.
GPT-3: Language Models are Few-Shot Learners (Paper Explained)

what is a language model: by simple words is a model that tries to predict on what comes next. It can generate Language in a probabilistic way.
Gpt-3 training has this datasets:
Common Crawl (filtered)
WebText2
Books1
Books2
Wikipedia
Common Crawl being a internet crawl, meaning most websites on the surface web are in this dataset,
the total sum of tokens on all of them is 499 billion tokens with 82%(410 billion tokens) being on the Common Crawl
Transformer Model: 
Transformers are designed to handle sequential data, like natural language, for tasks such as translation and text summarization however Transformers do not require that the sequential data be processed in order. For example, if the input data is a natural language sentence, the Transformer does not need to process the beginning of it before the end. Due to this feature, the Transformer allows for much more parallelization reducing training times. 
Now if I want to make a Transformer Model into a Language model from it: the input would be the context (meaning the sentence), the model creates several layer of attention mechanism (attention mechanism is basically a way where information is routes in between the different tokens) and as it goes up the layers the information is routed around and the model can make various inferences and at the end the model is suppose to come up with the next word of the sentence. This kind of model is an autoregressive language model meaning that is can go only left to right for the "autocompletion"
After a model choice you’d need fine tuning but GPT uses a different approach. They are using a Few-Shot Learners approach, for contrast:
zero-shot the model would predict the answer given only a natural language description of the task and no gradient update are performed, ex:
Translate English to French:			    ⇐ task description
Cheese ⇒  _____________                              ⇐ prompt
The reality is that here you are just hoping that the model has seen enough times this structure that it knows what it is meant to do.
One-shot in addition to the task description, the model sees a single example of the task and no gradient update are performed , ex:
Translate English to French:			  ⇐ task description
Sea otter ⇒ loutre de mer                                ⇐ example
Cheese ⇒ _____________                             ⇐ prompt
The advantage is that we need only one model and not needing to train a bunch of models for every single task, as we are providing a sort of training data with our example.
Few-shot similar to one-shot but the models see a few examples of the task. Also here not gradient update are performed , ex:
Translate English to French:			⇐ task description
Sea otter ⇒ loutre de mer                              ⇐ example
Peppermint ⇒ menthe poivrée                      ⇐ example
Plush giraffe ⇒girafe peluche                        ⇐ example
Cheese ⇒_____________                            ⇐ prompt
As this is the best solution for now only reason being is because of the enormity of the data that the current model of GPT is trained on, as this is not a viable solution for any other small model. You can see more and the result in the paper, this is just a short explanation on how the model works, and in the ambit of GPT these examples are called “priming”. (paper: https://arxiv.org/abs/2005.14165). 


From the examples on the internet I took inspiration and started trying to “prime” the model with some code and saw that for the simple functions it was fully capable of translating the code from different languages, from there I kept “priming” it and trying to make it more functional, until arriving at the point I’m now.
Why didn't I create my own model? 
If you do some research about gpt-3 you will see that the quantity of information and the computational power needed to make this kind of model is out of my reach, so I’m using their model “priming” it to add my information for then making it work for my purpose.

Here are some working examples that I made.


So the conclusion is that if the model keeps getting bigger and bigger as OpenAI is saying, future models are going to be exponentially better at it and with always more and more “priming” being done is just a question of how much time until it can translate the entire app even proprietary code.




Conclusion & recommendations; 

Reference

Code start:
python code_translation/code_translation.py

