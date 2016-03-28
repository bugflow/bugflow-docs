User Acceptance Testing
=======================

    As a Product Owner
    I need to know what the testing team thinks about a new release candidate
    So I can decide if it should be released into production or not.


Product Owner relies on the bugflow automation to deliver information about the testing that has occured on the release candidate. They use this to make their decision: should we deploy this version or not?

link - page about release candidate test report

The Product Owner is expecting this report, because the Release Manager coordinated the release candidate with them. The report is available to the Product Owner directly, or it may be delivered by the Release Manager.


Data Perspective
----------------

.. graphviz::

   digraph d{
      node [shape=rectangle];
      edge [arrowhead=crow];
      subgraph cluster_git {
         label="git";
	 repo [label="published\nrepository"];
	 rc [label="<<tag>>\nrelease\ncandidate"];
	 commit;
	 repo -> rc -> commit;
      }
      subgraph cluster_jenkins {
         label="Jenkins";
	 j [label="configured\ninstance"];
	 deployment [label="test env\ndeployment"];
	 j -> deployment;
      }
      subgraph cluster_gh {
         label="GitHub";
	 trq [label="test\nrequest"];
	 tt [label="test\ntask"];
	 ti [label="test\nincident"];
	 gvb [label="garden\nvariety\nbug"];
	 tt -> gvb [style=dashed];
	 trq -> tt -> ti;
      }
      subgraph cluster_bf {
         label="Bugflow UAT";
	 test_plan -> test_request -> uat_task;
	 test_plan -> uat_task_template -> uat_task;
	 uat_task_template -> checklist_item -> checklist_result;
	 uat_task -> checklist_result;
      }
      rc -> deployment -> test_request;
      uat_task -> tt;
      test_request -> trq;
      checklist_result -> ti;
   }


Ticket Perspective
------------------

There are three kinds of tickets associated with UAT:

* garden variety bugs.
* deployment summary/testing request ticket
* UAT task tickets

The garden variety bugs are any ticket raised in the usual way, that references the deployment summary. Testers might raise these as a side effect of UAT tasks, but they could be raised by anyone. They have a normal, organic ticket lifecycle.

The deployment summary ticket is triggered by the deployment process, which makes an API call to bugflow as part of the deployment automation. Bugflow then does a series of frightfullly clever things, resulting in the creation of an informative ticket.

link: page about the "testing request: $deployment_summary" ticket.

The UAT task tickets are simple tasks that reference the testing request ticket. They are subordinate tasks to that one. The task itself inks to a bugflow UI endpoint, which is a checklist-style UAT test plan. The tester fills in that form as they test the system, and when the form is completed a bugflow robot closes the ticket. As the form is being completed, I can see the ticket getting updated.


Test Manager Perspective
------------------------

It is "game on" when a deployment is created. I have many new tickets that I need to dispatch to testers. I can track the progress of my testers through the GitHub.

Alternatively, testers may self-assign. For example, there may be a rule that testers can be self-assigned to at-most $x UAT tickets at a time, but if there is no progress on a ticket in $y minutes they will be automatically unassigned by the bugflow bot.

If testing runs through to completion, all the tasks will be done. The most important job of the test manager is to abort the test using teh big red button interface. This will close all unfinished tests with status "aborted". When tests are aborted it means "Testing concludes this version should NOT get deployed to production".

link: big red button interface

