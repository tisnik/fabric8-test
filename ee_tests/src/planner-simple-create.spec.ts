import * as support from './support';
import { SpaceDashboardPage, SpacePipelinePage } from './page_objects';


describe('Planner Tab', () => {
  let spaceDashboard: SpaceDashboardPage;
  let spaceName: string;

  beforeEach( async () => {
    await support.desktopTestSetup();
    let login = new support.LoginInteraction();
    let mainDashboard = await login.run();

    spaceName = support.newSpaceName();
    spaceDashboard = await mainDashboard.createNewSpace(spaceName);

    // HACK: use this to reuse an existing space
    // spaceDashboard = new SpaceDashboardPage('foobar');
    // await spaceDashboard.open(PageOpenMode.RefreshBrowser);

  });


  it('can create a work item', async () => {
    let planner = await new SpacePipelinePage().gotoPlanTab();
    await planner.createWorkItem({
      title: 'Workitem Title',
      description: 'Describes the work item'
    });

    await planner.createWorkItem({
      title: 'Workitem Title',
      description: 'Describes the work item'
    });

  });

});

