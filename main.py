#!/usr/bin/env python3
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        # Root of the mindmap
        root = MindMapComposite( "This sure is a mindmap", "circle" )

        characters = MindMapComposite( "One branch", "oval" )
        characters.add( MindMapLeaf( "insert *wow*.mp3", "bang" ) )
        characters.add( MindMapLeaf( "incredible", "square" ) )
        characters.add( MindMapLeaf( "tbh this is cool that u can do this", "circle" ) )
        root.add( characters )

        plot_points = MindMapComposite( "Look its a second one", "square" )
        plot_points.add( MindMapLeaf( "this class is awesome", "bang" ) )
        plot_points.add( MindMapLeaf( "i knew programming was awesome but this class has opened my eyes", "oval" ) )
        plot_points.add( MindMapLeaf( "i mean makes sense in hindsight and foresight", "circle" ) )
        plot_points.add( MindMapLeaf( "cause like none of modern tech would be a thing without a computers ability to shenanigans", "square" ) )
        root.add( plot_points )

        themes = MindMapComposite( "Spoiler Owl", "cloud" )
        themes.add( MindMapLeaf( "Darth Vader is Luke's Father", "bang" ) )
        themes.add( MindMapLeaf( "Sheik is Zelda", "circle" ) )
        themes.add( MindMapLeaf( "Snape Kills Dumbledore", "square" ) )
        themes.add( MindMapLeaf( "There is No Queen of England", "cloud" ) )
        root.add( themes )

        setting = MindMapComposite( "Very know what im doing", "hexagon" )
        setting.add( MindMapLeaf( "Tbh i suck at abstract displays like this", "cloud" ) )
        setting.add( MindMapLeaf( "Youd think the opposite cause im an artistic person and want to computer games", "circle" ) )
        setting.add( MindMapLeaf( "but Autism™ make these things hard", "square" ) )
        setting.add( MindMapLeaf( "It's incredibly frustrating :D", "bang" ) )
        root.add( setting )

        conflicts = MindMapComposite( "Big wow", "bang" )
        conflicts.add( MindMapLeaf( "I hope this comes out looking like a clusterfuck", "diamond" ) )
        conflicts.add( MindMapLeaf( "now that i have this maybe ill use it for my projects in the future idk", "oval" ) )
        conflicts.add( MindMapLeaf( "will i be able to in a concise and useful way that will benefit my projects in the long run? probably not", "cloud" ) )
        root.add( conflicts )

        root.display()


if __name__ == "__main__":
    main()