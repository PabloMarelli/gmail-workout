import routine


class Workout(object):
    """An interface for a full workout. Typically this would be a full set of routines to do on a given day."""
    
    def __init__(self, name, routines):
        self.name = name
        self.routines = routines
        
    def as_html(self):
        """Helper method to format the routine as HTML.

        Returns:
            A `string` of HTML formatted workout routines.
        """
        routines_formatted = ''.join([routines.as_html() for routines in self.routines])
        return f"""
            <p><b>{self.name}</b></p>
            <p>Don't forget to <a href="https://youtube.com/watch?v=qQ96oXp5RTU">warm up</a>!</p>
            <ul>
                {routines_formatted}
            </ul>"""
            
    def __str__(self):
        return self.as_html()
    

MidEffortUpper = Workout(
    name="Mid Effort Upper Body",
    routines=[
        routine.Traps,
        routine.PressRoutine,
    ]
)