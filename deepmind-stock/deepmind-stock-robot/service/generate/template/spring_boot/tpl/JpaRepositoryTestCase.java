package ${obj.component.get_test_package_name()}.repository;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.Assert;

import ${obj.component.package_name()}.entity.${obj.name};
import ${obj.component.package_name()}.repository.${obj.project.repository}.${obj.name}Repository;
import com.faceye.test.feature.repository.BaseRepositoryTestCase;
/**
 * @说明:${obj.name} Repository 测试
 * @author @haipenge 
 * @联系:haipenge
 * @Create ${obj.get_current_date()}
 */
public class ${obj.name}RepositoryTestCase extends BaseRepositoryTestCase {
	@Autowired
	private ${obj.name}Repository ${obj.get_lower_start_clazz_name()}Repository = null;

	@Before
	public void before() throws Exception {
		this.${obj.get_lower_start_clazz_name()}Repository.deleteAll();
	}

	@After
	public void after() throws Exception {

	}

	@Test
	public void testSave() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Repository.save(${obj.get_lower_start_clazz_name()});
		Iterable<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Repository.findAll();
		Assert.isTrue(entities.iterator().hasNext());
	}

	@Test
	public void testDelete() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Repository.save(${obj.get_lower_start_clazz_name()});
        this.${obj.get_lower_start_clazz_name()}Repository.delete(${obj.get_lower_start_clazz_name()}.getId());
        Iterable<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Repository.findAll();
		Assert.isTrue(!entities.iterator().hasNext());
	}

	@Test
	public void testFindOne() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Repository.save(${obj.get_lower_start_clazz_name()});
		${obj.name} ${obj.name}=this.${obj.get_lower_start_clazz_name()}Repository.findOne(${obj.get_lower_start_clazz_name()}.getId());
		Assert.isTrue(${obj.name}!=null);
	}

	
}
