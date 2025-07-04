#!/usr/bin/python
# -*- coding: UTF-8 -*-

import git
import re
from types import ModuleType

def git_version( wd = "./", name = None, **options ):
    if isinstance( wd, ModuleType ):
        return git_version( wd.__path__[ 0 ], wd.__name__ )
    
    else:
        try:
            repo = git.Repo( wd, search_parent_directories = True )
            
        except git.exc.NoSuchPathError:
            return {}
        
        else:
            try:
                describe = repo.git.describe( "--dirty", options.get( "describe", None ) )
                commit_count = int( repo.git.rev_list( "--count", "HEAD" ) )
            
            except:
                describe = None
                commit_count = None
            
            finally:
                hash = repo.head.object.hexsha
                date = repo.git.log( "-1", "--date=iso", "--pretty=format:%cd" )
                 
                return {
                    'name': name,
                    'working_dir': repo.working_dir.replace( "\\", "/" ),
                    'commit_describe': describe,
                    'commit_count': commit_count,
                    'commit_hash': hash,
                    'commit_date': date
                }

def git_describe_split( describe ):
    try:
        return re.match( "^(.*)-([\d]+)-g([^-]*)(-(.*))?", describe ).groups()
    except:
        return None
