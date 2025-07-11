from io import StringIO
import sys

class Capturing( list ):
    def __enter__( self ):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    
    def __exit__( self, *args ):
        self.extend( self._stringio.getvalue().splitlines() )
        sys.stdout = self._stdout
        