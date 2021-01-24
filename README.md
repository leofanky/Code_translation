# Code_translation
 trying to translate kotlin to swift and vice versa with gpt-3
Introduction
- Importance of the Choice of the topic;
- Statement of the problem;
- Analytical Review of the state of the issue/ Literature Review;


Translation between the native languages of mobile development.
 As we all know we use our mobiles everyday and for almost everything now, but we all don’t have the same phone, I’m mostly talking about the two main operating systems that are in the market, that utilizes both their own proprietary language. As the two main players of this space we encounter Google with Android and Apple with iOS, the languages being Kotling and Swift.
=====main differences between kotling and swift======.
There are some solutions out there, like the flutter sdk with dart language you can create apps that can run in both operating system ( you can see an example in my github: leofanky/convo (github.com) ) because the final code is compile in native code but the functionality is really limited still and is not fully developed yet.
I found some project online trying to do a translation as an example: Gryphon, but it is only a preview and they don’t use ML or any other kind of new technologies. 
Main issue in the market is for small to medium companies that face the challenge of choosing a platform as there aren’t many developers that code in both and furthermore they are really requested and with a really high salary. So the idea would be to take your native code being Kotlin or Swift and translating to the other.





Main
-Description and justification of the Method;
-Presentation and analysis of the result;
- Analytical Comparison with already known result;


Why did I use a ML algorithm for code translation? 
 As the model I’m using is GPT-3, that is a language model that has been shown to do incredible things, such as translate human text to code and etc. From the examples I took inspiration and started trying to “prime” the model with simple transitions and saw that for the simple functions it was fully capable of doing so, from there I kept “priming” it and trying to make it more functional
Why didn't I create my own model? 
If you do some research about gpt-3 you will see that the quantity of information and the computational power needed to make this kind of model is out of my reach, so I’m using their pre trained model “priming” it to add my information for then making it work for my purpose.

Examples: (Videos and GIFS)


So the conclusion is that if the model keeps getting bigger and bigger asOpenAI is saying, future models are going to be exponentially better at it and with always more and more “priming” being done is just a question of how much time until it can translate the entire app even proprietary code.




Conclusion & recommendations; 

Reference

Code:

