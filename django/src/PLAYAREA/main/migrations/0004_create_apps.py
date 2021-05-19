from django.db import migrations


def create_apps(apps, schema_editor):
    from main.models import App, SubApp

    accounts: App = App.objects.create(
        name='Accounts', name_stringified=None, href='accounts/'
    )
    accounts.save()

    karnevalsorden_editor: App = App.objects.create(
        name='Karnevalsorden Editor', name_stringified=None, href='karnevalsorden-editor'
    )
    karnevalsorden_editor.save()

    threejs: App = App.objects.create(
        name='Three JS Playground', name_stringified='ThreeJSPlayground', href='threejs_tests/')
    threejs.save()

    subThreejs001: SubApp = SubApp.objects.create(
        name='Test ThreeJS 001', name_stringified=None, href='test-threejs-001/'
    )
    subThreejs001.save()

    subThreejs002: SubApp = SubApp.objects.create(
        name='Test ThreeJS 002', name_stringified=None, href='test-threejs-002/'
    )
    subThreejs002.save()

    subThreejs003: SubApp = SubApp.objects.create(
        name='Test ThreeJS Car', name_stringified=None, href='test-threejs-car/'
    )
    subThreejs003.save()

    threejs.subApps.add(subThreejs001)
    threejs.subApps.add(subThreejs002)
    threejs.subApps.add(subThreejs003)
    threejs.save()

    vuejs: App = App.objects.create(
        name='Vue Playground', name_stringified='VuePlayground', href='vue_tests/'
    )

    subVue001: SubApp = SubApp.objects.create(
        name='Test Vue 001', name_stringified=None, href='vue-test-001/'
    )
    subVue001.save()

    subVue002: SubApp = SubApp.objects.create(
        name='Test Vue 002', name_stringified=None, href='vue-test-002/'
    )
    subVue002.save()

    subVue003: SubApp = SubApp.objects.create(
        name='Test Vue 003', name_stringified=None, href='vue-test-003/'
    )
    subVue003.save()

    subVueModal001: SubApp = SubApp.objects.create(
        name='Test Vue Modal 001', name_stringified=None, href='vue-test-modal-001/'
    )
    subVueModal001.save()

    vuejs.subApps.add(subVue001)
    vuejs.subApps.add(subVue002)
    vuejs.subApps.add(subVue003)
    vuejs.subApps.add(subVueModal001)
    vuejs.save()

    various: App = App.objects.create(
        name='Various', name_stringified='Various', href='various/',
    )

    subVariousPureComp: SubApp = SubApp.objects.create(
        name='Pure JS Component', name_stringified=None, href='pure-js-component'
    )
    subVariousPureComp.save()

    subVariousDateRangePick: SubApp = SubApp.objects.create(
        name='DateRangePicker', name_stringified=None, href='daterangepicker/'
    )
    subVariousDateRangePick.save()

    subVariosTestRpc: SubApp = SubApp.objects.create(
        name='Test RPC 1',
        name_stringified=None,
        href='test-rpc-1'
    )

    various.subApps.add(subVariousPureComp)
    various.subApps.add(subVariousDateRangePick)
    various.subApps.add(subVariosTestRpc)
    various.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_app_subapp')
    ]

    operations = [migrations.RunPython(create_apps)]
