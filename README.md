# TechArena
A python script to solve the next problem:

```You are given a polygon with n vertices (without self-intersection) on a plane. You need to find a set of rectangles such that their union fully contains the given polygon. Sides of the rectangles must be parallel to the axis. Rectangles can intersect.

The union of rectangles fully contains the given polygon if each point of the polygon (including inner points, sides, and vertices) lies inside or on a side of some rectangle.

Each rectangle in the set takes some time to be processed. If the rectangle lies fully inside the polygon, then the time is 1 + c1⋅RectangleArea, if not — the time is 1+c2⋅RectangleArea. It is known that c1<c2.

The score of the set of rectangles you found is the total process time taken for each rectangle. Your goal is to find a set of rectangles that fully covers the given polygon and minimizes the score.
